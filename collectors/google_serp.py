import os
import re
from urllib.parse import urlparse

import requests


def _domain_from_url(url: str) -> str | None:
    try:
        host = urlparse(url).netloc.lower()
        host = host.replace("www.", "")
        return host if host else None
    except Exception:
        return None


def _extract_domains_from_serpapi(ads: list[dict], max_domains: int) -> list[str]:
    domains = []
    for ad in ads or []:
        for key in ("displayed_link", "link", "tracking_link"):
            raw = ad.get(key)
            if not raw:
                continue

            # displayed_link às vezes vem sem http (ex: "example.com/xyz")
            if raw.startswith("http"):
                d = _domain_from_url(raw)
            else:
                m = re.search(r"([a-z0-9-]+\.[a-z]{2,})", raw.lower())
                d = m.group(1) if m else None

            if d:
                domains.append(d)
                break

        if len(domains) >= max_domains:
            break

    # unique preservando ordem
    seen = set()
    out = []
    for d in domains:
        if d not in seen:
            seen.add(d)
            out.append(d)
    return out


async def collect_serp(cfg: dict, keyword: str, city: str, uf: str, device: str, max_domains: int = 30) -> dict:
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        raise RuntimeError("SERPAPI_API_KEY não configurada")

    params = {
        "engine": "google",
        "q": keyword,
        "hl": "pt",
        "gl": "br",
        "api_key": api_key,
    }

    # SerpAPI: para mobile, enviar device=mobile; para desktop, omitir
    if device == "mobile":
        params["device"] = "mobile"

    # IMPORTANTE: removemos location por enquanto porque a SerpAPI rejeitou "São Paulo, SP, Brazil"
    # (você ainda pode manter city/uf no output para segmentar o relatório internamente)

    r = requests.get("https://serpapi.com/search.json", params=params, timeout=30)

    if r.status_code >= 400:
        # mostra motivo no log do Actions
        try:
            print("[SERPAPI ERROR]", r.status_code, r.text[:1200])
        except Exception:
            pass
        r.raise_for_status()

    data = r.json()

    ads = data.get("ads") or data.get("top_ads") or []
    domains = _extract_domains_from_serpapi(ads, max_domains=max_domains)

    return {
        "keyword": keyword,
        "city": city,
        "uf": uf,
        "device": device,
        "has_ads": bool(domains),
        "domains": domains,
        "source": "serpapi"
    }
