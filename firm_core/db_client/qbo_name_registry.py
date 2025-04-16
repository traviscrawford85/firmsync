import sqlite3
from datetime import datetime

class QBORegistryDBClient:
    def __init__(self, db_path="qbo.sqlite3"):
        self.conn = sqlite3.connect(db_path)
        self.create_registry_table()

    def create_registry_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS qbo_name_registry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            qbo_id TEXT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            source TEXT NOT NULL,
            source_id TEXT,
            matter_display_number TEXT,
            synced_at TIMESTAMP,
            notes TEXT
        );
        """)
        self.conn.commit()

    def register_name(self, name, type_, qbo_id=None, source="clio", source_id=None, matter_display_number=None, notes=None):
        now = datetime.now()
        self.conn.execute("""
            INSERT INTO qbo_name_registry (qbo_id, name, type, source, source_id, matter_display_number, synced_at, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (qbo_id, name, type_, source, source_id, matter_display_number, now, notes))
        self.conn.commit()

    def name_exists(self, name) -> bool:
        result = self.conn.execute("""
            SELECT 1 FROM qbo_name_registry WHERE name = ?
        """, (name,)).fetchone()
        return result is not None
