import asyncio
from fastapi import FastAPI
import sqlite3

from producer import fetch_and_send_exchange_rate
from database import init_db

app = FastAPI(title="Async Real-Time Exchange Platform")

# -----------------------------
# Async background scheduler
# -----------------------------
async def hourly_scheduler():
    while True:
        print("⏱️ Fetching exchange rate...")
        try:
            fetch_and_send_exchange_rate()
        except Exception as e:
            print("❌ Error:", e)

        await asyncio.sleep(3600)  # 1 heure

# -----------------------------
# Startup event
# -----------------------------
@app.on_event("startup")
async def startup_event():
    init_db()
    asyncio.create_task(hourly_scheduler())

# -----------------------------
# API
# -----------------------------
@app.get("/alerts")
async def get_alerts():
    conn = sqlite3.connect("realtime.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT timestamp, rate, variation
        FROM exchange_rate_alerts
        ORDER BY timestamp DESC
        LIMIT 10
    """)

    rows = cur.fetchall()
    conn.close()

    return rows
