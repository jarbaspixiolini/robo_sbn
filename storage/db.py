import sqlite3
from pathlib import Path

DB_PATH = Path("artifacts") / "monitor.db"

def conn():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db():
    with conn() as c:
        c.execute("""
        CREATE TABLE IF NOT EXISTS serp_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            keyword TEXT NOT NULL,
            city TEXT NOT NULL,
            uf TEXT NOT NULL,
            device TEXT NOT NULL,
            has_ads INTEGER NOT NULL,
            domains TEXT
        )
        """)
        c.execute("""
        CREATE TABLE IF NOT EXISTS seen_domains (
            domain TEXT PRIMARY KEY,
            first_seen_ts TEXT NOT NULL,
            last_seen_ts TEXT NOT NULL
        )
        """)
