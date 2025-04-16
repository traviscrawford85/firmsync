# firm_core/cache/cache_manager.py

import sqlite3
from pathlib import Path
from typing import Dict, Any, List, Optional


class CacheManager:
    def __init__(self, db_path: str = "clio_cache.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row  # Dict-like access
        self.cur = self.conn.cursor()
        print(f"📦 Connected to local cache → {Path(self.db_path).resolve()}")

    def ensure_table(self, table_name: str, schema: Dict[str, str]):
        """
        Ensures a table exists. `schema` should be a dict like:
        {"id": "INTEGER PRIMARY KEY", "name": "TEXT", "email": "TEXT"}
        """
        fields = ", ".join(f"{col} {type}" for col, type in schema.items())
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})"
        self.cur.execute(sql)
        self.conn.commit()
        print(f"🛠️  Ensured table '{table_name}'")

    def insert(self, table_name: str, data: Dict[str, Any]):
        """
        Insert or replace a row into the table.
        """
        cols = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        sql = f"INSERT OR REPLACE INTO {table_name} ({cols}) VALUES ({placeholders})"
        self.cur.execute(sql, tuple(data.values()))
        self.conn.commit()

    def bulk_insert(self, table_name: str, rows: List[Dict[str, Any]]):
        """
        Bulk insert a list of dictionaries.
        """
        if not rows:
            return
        for row in rows:
            self.insert(table_name, row)

    def fetch(self, table_name: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Fetch rows as a list of dictionaries.
        """
        sql = f"SELECT * FROM {table_name} LIMIT ?"
        self.cur.execute(sql, (limit,))
        return [dict(row) for row in self.cur.fetchall()]

    def query(self, table_name: str, where_clause: str = "", params: Optional[tuple] = ()) -> List[Dict[str, Any]]:
        sql = f"SELECT * FROM {table_name}"
        if where_clause:
            sql += f" WHERE {where_clause}"
        self.cur.execute(sql, params)
        return [dict(row) for row in self.cur.fetchall()]

    def close(self):
        self.conn.close()
        print("🔒 Cache connection closed.")
