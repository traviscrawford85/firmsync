import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent / "qbo_sync.sqlite3"


TABLES_SQL = {
    "qbo_purchases": """
    CREATE TABLE IF NOT EXISTS qbo_purchases (
        id TEXT PRIMARY KEY,
        clio_activity_id TEXT UNIQUE,
        vendor_id TEXT,
        customer_id TEXT,
        amount REAL,
        description TEXT,
        synced_at TIMESTAMP,
        qbo_purchase_id TEXT,
        error TEXT
    );
    """,
    "qbo_vendors": """
    CREATE TABLE IF NOT EXISTS qbo_vendors (
        id TEXT PRIMARY KEY,
        name TEXT UNIQUE,
        qbo_id TEXT
    );
    """,
    "qbo_customers": """
    CREATE TABLE IF NOT EXISTS qbo_customers (
        id TEXT PRIMARY KEY,
        name TEXT UNIQUE,
        parent_id TEXT,
        qbo_id TEXT
    );
    """
}


def initialize_database(db_path: Path = DB_PATH):
    print(f"🔧 Initializing QBO Sync DB at {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for name, ddl in TABLES_SQL.items():
        print(f"📦 Creating table: {name}")
        cursor.execute(ddl)

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()
