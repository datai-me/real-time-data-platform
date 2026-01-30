import sqlite3

DB_NAME = "realtime.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS exchange_rate_alerts (
        timestamp REAL,
        rate REAL,
        variation REAL
    )
    """)

    conn.commit()
    conn.close()
