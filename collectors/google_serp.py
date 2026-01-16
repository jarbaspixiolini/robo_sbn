import os
import re
from urllib.parse import urlparse
import requests
async def collect_serp(cfg: dict, keyword: str, city: str, uf: str, device: str, max_domains: int = 30) -> dict:
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        raise RuntimeError("SERPAPI_API_KEY não configurada")

    params = {
        "engine": "google",
        "q": keyword,
        "hl": "pt",
        "gl": "br",
        # location às vezes é sensível; mantemos e temos fallback
        "location": f"{city}, {uf}, Brazil",
        "api_key": api_key,
    }

    # SerpAPI: para mobile, enviar device=mobile; para desktop, omitir o parâmetro
    if device == "mobile":
        params["device"] = "mobile"

    r = requests.get("https://serpapi.com/search.json", params=params, timeout=30)

    # Se der erro, printa o corpo para diagnosticar (aparece no log do Actions)
    if r.status_code >= 400:
        try:
            print("[SERPAPI ERROR]", r.status_code, r.text[:1200])
        except Exception:
            pass

        # Fallback: remove location e tenta de novo (muitas vezes resolve 400)
        if "location" in params:
            params.pop("location", None)
            r = requests.get("https://serpapi.com/search.json", params=params, timeout=30)
            if r.status_code >= 400:
                try:
                    print("[SERPAPI ERROR - FALLBACK]", r.status_code, r.text[:1200])
                except Exception:
                    pass
                r.raise_for_status()
        else:
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
