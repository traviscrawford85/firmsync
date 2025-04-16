import sqlite3
import json
from rich.table import Table
from rich.console import Console

def preview_contacts(conn, limit=10):
    cursor = conn.cursor()
    cursor.execute("SELECT id, json FROM Contacts LIMIT ?", (limit,))
    rows = cursor.fetchall()

    table = Table(title=f"Clio Contacts Preview (Limit {limit})")
    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Name", style="green")
    table.add_column("Email", style="magenta")

    for row in rows:
        contact_id = row["id"]
        json_data = json.loads(row["json"])
        name = json_data.get("Name", "—")
        email = json_data.get("Primary_Email_Address", "—")

        table.add_row(str(contact_id), name, email)

    Console().print(table)
