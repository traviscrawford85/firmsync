import sqlite3
from typing import Optional, List
from datetime import datetime
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent / "local_db" / "qbo_sync.sqlite3"


class QBOSyncDBClient:
    def __init__(self, db_path: Path = DB_PATH):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def get_synced_activity_ids(self) -> set:
        rows = self.conn.execute(
            "SELECT clio_activity_id FROM qbo_purchases"
        ).fetchall()
        return set(row["clio_activity_id"] for row in rows)

    def insert_purchase_sync(
        self,
        clio_activity_id: str,
        amount: float,
        qbo_purchase_id: str,
        vendor_id: str,
        customer_id: str,
        description: str,
        error: Optional[str] = None,
    ):
        self.conn.execute(
            """
            INSERT OR REPLACE INTO qbo_purchases (
                id, clio_activity_id, amount, qbo_purchase_id,
                vendor_id, customer_id, description, synced_at, error
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                f"sync-{clio_activity_id}",
                clio_activity_id,
                amount,
                qbo_purchase_id,
                vendor_id,
                customer_id,
                description,
                datetime.utcnow().isoformat(),
                error,
            ),
        )
        self.conn.commit()

    def insert_vendor(self, name: str, qbo_id: str):
        self.conn.execute(
            "INSERT OR IGNORE INTO qbo_vendors (id, name, qbo_id) VALUES (?, ?, ?)",
            (f"vendor-{qbo_id}", name, qbo_id),
        )
        self.conn.commit()

    def insert_customer(self, name: str, qbo_id: str, parent_id: Optional[str] = None):
        self.conn.execute(
            "INSERT OR IGNORE INTO qbo_customers (id, name, qbo_id, parent_id) VALUES (?, ?, ?, ?)",
            (f"cust-{qbo_id}", name, qbo_id, parent_id),
        )
        self.conn.commit()

    def get_vendor_id_by_name(self, name: str) -> Optional[str]:
        row = self.conn.execute(
            "SELECT qbo_id FROM qbo_vendors WHERE name = ?", (name,)
        ).fetchone()
        return row["qbo_id"] if row else None

    def get_customer_id_by_name(self, name: str) -> Optional[str]:
        row = self.conn.execute(
            "SELECT qbo_id FROM qbo_customers WHERE name = ?", (name,)
        ).fetchone()
        return row["qbo_id"] if row else None
