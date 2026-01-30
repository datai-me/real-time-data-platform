import sqlite3

conn = sqlite3.connect("realtime.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS exchange_rates (
    timestamp REAL,
    rate REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS exchange_rate_alerts (
    timestamp REAL,
    rate REAL,
    variation REAL
)
""")

conn.commit()
conn.close()

print("Base SQLite initialisée")
