from typing import List
from clio_sdk.api.matters_api import MattersApi
from auth.clio_auth import get_authenticated_api_client # your wrapped auth
from custom_models.matter import MatterModel  # renamed for consistency

class MatterService:
    def __init__(self):
        self.client = get_authenticated_api_client()
        self.api = MattersApi(self.client)

    def get_recent_matters(self, limit: int = 10) -> List[MatterModel]:
        """
        Fetches recent matters from Clio and parses them into MatterModel instances.
        """
        response = self.api.matter_index(limit=limit)
        raw_matters = response.data

        matters = []
        for item in raw_matters:
            matter = MatterModel(
                id=item.id,
                display_number=item.attributes.display_number,
                description=item.attributes.description,
                status=item.attributes.status,
                client_name=item.attributes.client.get('name') if item.attributes.client else None,
                practice_area=item.attributes.practice_area.get('name') if item.attributes.practice_area else None
            )
            matters.append(matter)

        return matters

    def get_matter_by_id(self, matter_id: int) -> MatterModel:
        """
        Fetches a single matter by ID and parses it into a MatterModel.
        """
        item = self.api.matter_show(matter_id).data

        return MatterModel(
            id=item.id,
            display_number=item.attributes.display_number,
            description=item.attributes.description,
            status=item.attributes.status,
            client_name=item.attributes.client.get('name') if item.attributes.client else None,
            practice_area=item.attributes.practice_area.get('name') if item.attributes.practice_area else None
        )
