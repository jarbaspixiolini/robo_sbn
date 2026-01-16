import os
import requests

def send_slack(text: str) -> bool:
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook:
        print("[SLACK] SLACK_WEBHOOK_URL não configurado.")
        return False

    try:
        r = requests.post(webhook, json={"text": text}, timeout=20)
        print(f"[SLACK] status={r.status_code}")
        if r.status_code >= 300:
            print(f"[SLACK] body={r.text[:500]}")
            r.raise_for_status()
        return True
    except Exception as e:
        print(f"[SLACK] exception={e}")
        raise
