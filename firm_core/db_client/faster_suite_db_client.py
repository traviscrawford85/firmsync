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

    # Get Vendor Contacts
    def get_company_contacts(self):
        query = """
            SELECT 
                ID,
                json_extract(Data, '$.Name') as name,
                json_extract(Data, '$.Type') as type,
                json_extract(Data, '$.Primary_Email_Address') as email,
                json_extract(Data, '$.Primary_Phone_Number') as phone
            FROM Contacts
            WHERE json_extract(Data, '$.Type') = 'Company'
        """
        return self.conn.execute(query).fetchall()


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

    def get_contacts_tagged_as_vendor(self):
        query = """
            SELECT 
                ID,
                json_extract(Data, '$.Name') AS name,
                json_extract(Data, '$.Type') AS type,
                json_extract(Data, '$.Primary_Email_Address') AS email
            FROM Contacts
            WHERE json_extract(Data, '$.Tags') LIKE '%vendor%'
        """
        return self.conn.execute(query).fetchall()

    def get_contacts_with_no_matters(self):
        query = """
            SELECT 
                c.ID,
                json_extract(c.Data, '$.Name') AS name,
                json_extract(c.Data, '$.Type') AS type
            FROM Contacts c
            LEFT JOIN MatterContacts mc ON mc.Contact_ID = c.ID
            WHERE mc.Contact_ID IS NULL
        """
        return self.conn.execute(query).fetchall()

    def get_probable_vendors(self):
        query = """
            SELECT 
                c.ID,
                json_extract(c.Data, '$.Name') AS name,
                json_extract(c.Data, '$.Type') AS type,
                json_extract(c.Data, '$.Primary_Email_Address') AS email
            FROM Contacts c
            LEFT JOIN MatterContacts mc ON mc.Contact_ID = c.ID
            WHERE mc.Contact_ID IS NULL
            AND json_extract(c.Data, '$.Type') = 'Company'
        """
        return self.conn.execute(query).fetchall()

    def get_all_contacts_with_metadata(self) -> List[Dict]:
        query = """
            SELECT 
                c.ID as id,
                json_extract(c.Data, '$.Name') AS name,
                json_extract(c.Data, '$.Type') AS type,
                json_extract(c.Data, '$.Tags') AS tags,
                (
                    SELECT COUNT(*) 
                    FROM MatterContacts mc 
                    WHERE mc.Contact_ID = c.ID
                ) AS matter_count
            FROM Contacts c
        """
        results = self.conn.execute(query).fetchall()
        return [dict(row) for row in results]
