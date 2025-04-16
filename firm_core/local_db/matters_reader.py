from .table_iterator import TableIterator

class MattersReader:
    def __init__(self, conn):
        self.conn = conn

    def all(self, limit=100):
        return TableIterator(self.conn, "Matters", limit=limit, parse_json_column="json")

    def find_by_name(self, name):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Matters WHERE name LIKE ?", (f"%{name}%",))
        return cur.fetchall()

    def get_primary_email(self, contact_id):
        cur = self.conn.cursor()
        cur.execute("SELECT json FROM Matters WHERE id = ?", (contact_id,))
        row = cur.fetchone()
        if row:
            import json
            json_data = json.loads(row["json"])
            return json_data.get("Primary_Email_Address")
        return None
