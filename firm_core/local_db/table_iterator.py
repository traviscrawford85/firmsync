import sqlite3
import json

class TableIterator:
    def __init__(self, conn, table_name, limit=100, parse_json_column=None):
        """
        Initialize an iterator for any SQLite table.

        Args:
            conn (sqlite3.Connection): Open SQLite connection.
            table_name (str): The table to iterate over.
            limit (int): Page size (batch size).
            parse_json_column (str or None): Optional column to parse as JSON.
        """
        self.conn = conn
        self.table = table_name
        self.limit = limit
        self.offset = 0
        self.parse_json_column = parse_json_column

    def __iter__(self):
        return self

    def __next__(self):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM {self.table} LIMIT ? OFFSET ?", (self.limit, self.offset))
        rows = cur.fetchall()

        if not rows:
            raise StopIteration

        self.offset += self.limit
        col_names = [desc[0] for desc in cur.description]

        # Convert to list of dicts
        dict_rows = [dict(zip(col_names, row)) for row in rows]

        if self.parse_json_column:
            for row in dict_rows:
                try:
                    row[self.parse_json_column] = json.loads(row[self.parse_json_column])
                except (TypeError, json.JSONDecodeError):
                    pass  # Leave as-is if not valid JSON

        return dict_rows
