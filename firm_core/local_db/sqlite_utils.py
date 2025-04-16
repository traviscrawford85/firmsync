import sqlite3
from pathlib import Path

def get_readonly_connection(db_path: str):
    """
    Open a read-only SQLite connection using URI format.
    """
    uri_path = Path(db_path).resolve().as_uri().replace("file:///", "file:/")
    return sqlite3.connect(f"{uri_path}?mode=ro", uri=True)
