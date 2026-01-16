import os
import requests

def send_slack(text: str) -> bool:
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook:
        return False

    r = requests.post(webhook, json={"text": text}, timeout=20)
    r.raise_for_status()
    return True
