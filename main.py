from fastapi import FastAPI
import sqlite3

app = FastAPI(title="Exchange Rate API")

@app.get("/alerts")
def get_alerts():
    conn = sqlite3.connect("realtime.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT timestamp, rate, variation
        FROM exchange_rate_alerts
        ORDER BY timestamp DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows
