from typing import List, Dict, Optional
from firm_clio.clio_client import get_clio_service
from custom_services.matter_service import MatterService
from typing import Optional, List



class ClioFacade:
    """
    Facade for Clio Manage API operations.
    Encapsulates all data retrieval logic from Clio.
    """
    

    def __init__(self):
        self.services = get_clio_service()



    def get_matter_by_id(self, matter_id: int):
        return self.services.get_matter_by_id(matter_id)

    def get_recent_matters(self, limit: int = 10):
        return self.services.get_recent_matters(limit=limit)

    def get_matters_by_client_id(self, client_id: int):
        return self.services.get_matters_by_client_id(client_id)

    def get_all_matters_by_practice_area(self, practice_area: str) -> List[Dict]:
        """Return all matters filtered by a specific practice area."""
        raise NotImplementedError("get_all_matters_by_practice_area is not yet implemented.")
    
    def update_matter(self, matter_id: int, update_data: Dict) -> Dict:
        """PATCH a matter with new data."""
        raise NotImplementedError("update_matter is not yet implemented.")

    # 📋 TASKS
    def get_tasks_by_matter(self, matter_id: int, status: Optional[str] = None) -> List[Dict]:
        """Return tasks assigned to a matter, optionally filtered by status."""
        raise NotImplementedError("get_tasks_by_matter is not yet implemented.")
        

    def delete_tasks_by_matter(self, matter_id: int) -> None:
        """Delete all tasks associated with a matter (looped DELETE)."""
        raise NotImplementedError("delete_tasks_by_matter is not yet implemented.")
        

    # 🧩 CUSTOM FIELDS
    def get_custom_field_by_id(self, field_id: int) -> Dict:
        """Retrieve metadata for a single custom field."""
        raise NotImplementedError("get_custom_field_by_id is not yet implemented.")

    def get_contact_by_id(self, contact_id: int) -> Optional[Dict]:
        """Fetch a contact by Clio contact ID."""
        raise NotImplementedError("get_contact_by_id is not yet implemented.")

    def get_contact_by_name(self, name: str) -> List[Dict]:
        """Search for contacts by name."""
        raise NotImplementedError("get_contact_by_name is not yet implemented.")

    def get_all_contacts(self) -> List[Dict]:
        """Return a list of all contacts."""
        raise NotImplementedError("get_all_contacts is not yet implemented.")
