import sqlite3
from pathlib import Path
from .contacts_reader import ContactsReader
from .matters_reader import MattersReader
from firm_core.local_db.sqlite_utils import get_readonly_connection


def get_readonly_connection(db_path: str):
    """
    Open a read-only SQLite connection using URI format.
    """
    uri_path = Path(db_path).resolve().as_uri().replace("file:///", "file:/")
    conn = sqlite3.connect(f"{uri_path}?mode=ro", uri=True)
    return conn

class ClioReadOnlyDB:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row  # for dict-like access
        self._contacts = ContactsReader(self.conn)
        self._matters = MattersReader(self.conn)

    @property
    def contacts(self):
        return self._contacts

    @property
    def matters(self):
        return self._matters
    

    def close(self):
        self.conn.close()
