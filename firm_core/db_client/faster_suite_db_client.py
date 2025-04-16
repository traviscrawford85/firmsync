from firm_core.local_db.clio_read_only_db import get_readonly_connection
from firm_core.local_db.contacts_reader import ContactsReader
from firm_core.local_db.matters_reader import MattersReader
from rich.table import Table
from rich.console import Console
import sqlite3


class FasterSuiteDBClient:
    """
    High-level client for reading from Faster Suite's Clio SQLite cache.
    Provides simple methods to browse cached Clio data from the local DB.
    """
    def __init__(self, db_path="clio.sqlite3"):
        self.conn = get_readonly_connection(db_path)

    def contacts(self, limit=10):
        contacts = ContactsReader(self.conn).all(limit=limit)

        table = Table(title=f"Clio Contacts (Limit: {limit})")
        table.add_column("ID", justify="right", style="dim")
        table.add_column("Name", style="cyan")
        table.add_column("Email", style="magenta")

        for contact in contacts:
            table.add_row(str(contact.id), contact.name or "—", contact.email or "—")

        Console().print(table)
        return contacts

    def matters(self, limit=10):
        matters = MattersReader(self.conn).all(limit=limit)

        table = Table(title=f"Clio Matters (Limit: {limit})")
        table.add_column("ID", justify="right", style="dim")
        table.add_column("Display Number", style="cyan")
        table.add_column("Description", style="green")

        for matter in matters:
            table.add_row(str(matter.id), matter.display_number or "—", matter.description or "—")

        Console().print(table)
        return matters
