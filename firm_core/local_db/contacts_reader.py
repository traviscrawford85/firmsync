from .table_iterator import TableIterator
from firm_core.local_db.sqlite_utils import get_readonly_connection

from rich.table import Table
from rich.console import Console

class ContactsReader:
    def __init__(self, conn):
        self.conn = conn

    def all(self, limit=100):
        return TableIterator(self.conn, "Contacts", limit=limit, parse_json_column="json")

    def find_by_name(self, name):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Contacts WHERE name LIKE ?", (f"%{name}%",))
        return cur.fetchall()

    def get_primary_email(self, contact_id):
        cur = self.conn.cursor()
        cur.execute("SELECT json FROM Contacts WHERE id = ?", (contact_id,))
        row = cur.fetchone()
        if row:
            import json
            json_data = json.loads(row["json"])
            return json_data.get("Primary_Email_Address")
        return None
