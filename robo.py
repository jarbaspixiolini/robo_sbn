import os
import json
import yaml
import asyncio
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from storage.db import init_db, conn
from collectors.google_serp import collect_serp
from alerts.slack import send_slack


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_config():
    with open("config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def upsert_seen_domain(domain: str, ts: str) -> bool:
    """
    Retorna True se for domínio novo (primeira vez visto).
    """
    with conn() as c:
        row = c.execute("SELECT domain FROM seen_domains WHERE domain = ?", (domain,)).fetchone()
        if row:
            c.execute("UPDATE seen_domains SET last_seen_ts = ? WHERE domain = ?", (ts, domain))
            return False
        else:
            c.execute(
                "INSERT INTO seen_domains(domain, first_seen_ts, last_seen_ts) VALUES(?,?,?)",
                (domain, ts, ts),
            )
            return True


def executive_summary(ts: str) -> str:
    """
    Gera um resumo executivo da execução atual (ts),
    baseado no que foi gravado no SQLite.
    """
    with conn() as c:
        total_runs = c.execute("SELECT COUNT(*) FROM serp_runs WHERE ts = ?", (ts,)).fetchone()[0]
        ads_runs = c.execute("SELECT COUNT(*) FROM serp_runs WHERE ts = ? AND has_ads = 1", (ts,)).fetchone()[0]

        # Coleta todos os domínios (ads) desta execução
        rows = c.execute(
            "SELECT domains FROM serp_runs WHERE ts = ? AND has_ads = 1", (ts,)
        ).fetchall()

        all_domains = []
        for (domains_json,) in rows:
            if not domains_json:
                continue
            try:
                all_domains.extend(json.loads(domains_json))
            except Exception:
                pass

        # Frequência por domínio
        freq = {}
        for d in all_domains:
            freq[d] = freq.get(d, 0) + 1

        top = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:8]

        unique_domains = c.execute("SELECT COUNT(*) FROM seen_domains").fetchone()[0]

    pct_ads = (ads_runs / total_runs * 100) if total_runs else 0

    lines = []
    lines.append("*Conexa Monitor — Resumo Executivo*")
    lines.append(f"Execução (UTC): `{ts}`")
    lines.append(f"Buscas: *{total_runs}* | Com anúncios: *{ads_runs}* ({pct_ads:.0f}%)")
    lines.append(f"Domínios únicos no histórico: *{unique_domains}*")

    if top:
        lines.append("")
        lines.append("*Top anunciantes (recorrência nesta execução)*")
        for domain, count in top:
            lines.append(f"• `{domain}` — {count} ocorrência(s)")
    else:
        lines.append("")
        lines.append("Nenhum anúncio detectado nesta execução.")

    return "\n".join(lines)


async def main():
    load_dotenv()
    init_db()

    # Garante que artifacts exista (para upload no Actions)
    Path("artifacts").mkdir(exist_ok=True)

    cfg = load_config()
    keywords = cfg["keywords"]
    capitals = cfg["capitals_sul_sudeste"]
    devices = cfg["devices"]
    max_serp_domains = cfg["limits"]["serp_results_per_run"]

    ts = now_iso()

    new_domains = []
    results_count = 0

    print(f"[{ts}] Iniciando monitoramento...")
    print(f"Keywords={len(keywords)} | Cidades={len(capitals)} | Devices={len(devices)}")

    # Loop principal
    for device in devices:
        for kw in keywords:
            for cap in capitals:
                city, uf = cap["name"], cap["uf"]

                result = await collect_serp(cfg, kw, city, uf, device, max_domains=max_serp_domains)
                results_count += 1

                # Grava no DB
                with conn() as c:
                    c.execute(
                        "INSERT INTO serp_runs(ts, keyword, city, uf, device, has_ads, domains) VALUES(?,?,?,?,?,?,?)",
                        (
                            ts,
                            result["keyword"],
                            result["city"],
                            result["uf"],
                            result["device"],
                            1 if result["has_ads"] else 0,
                            json.dumps(result["domains"], ensure_ascii=False),
                        ),
                    )

                # Detecta domínios novos
                for d in result["domains"]:
                    if upsert_seen_domain(d, ts):
                        new_domains.append(
                            {"domain": d, "keyword": kw, "city": city, "uf": uf, "device": device}
                        )

    print(f"Execução concluída. Total buscas: {results_count}. Novos domínios: {len(new_domains)}")

    # 1) (Opcional) alerta de novos domínios
    if new_domains:
        lines = [f"*Conexa Monitor* — {len(new_domains)} novo(s) domínio(s) detectado(s):"]
        for item in new_domains[:10]:
            lines.append(
                f"• `{item['domain']}` — *{item['keyword']}* | {item['city']}-{item['uf']} ({item['device']})"
            )
        if len(new_domains) > 10:
            lines.append(f"... e mais {len(new_domains) - 10} (ver DB)")

        try:
            send_slack("\n".join(lines))
        except Exception as e:
            print(f"[WARN] Falha ao enviar alerta de novos domínios: {e}")

    # 2) resumo executivo (sempre envia)
    try:
        send_slack(executive_summary(ts))
    except Exception as e:
        print(f"[WARN] Falha ao enviar resumo executivo: {e}")


if __name__ == "__main__":
    asyncio.run(main())


