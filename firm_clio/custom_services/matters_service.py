from typing import List
from clio_sdk.api.matters_api import MattersApi
from clio_sdk import Configuration, ApiClient
from utils.token_storage import load_token_data  # ✅ Centralized helper now in use
from firm_clio.custom_models.matter import MatterModel  # Your custom model
from firm_clio.clio_client import get_clio_client  # ✅ this works with token

class MatterService:
    def __init__(self):
        self.client = get_clio_client()  # ✅ Authorized client
        self.api = MattersApi(self.client)


    def get_recent_matters(self, limit: int = 10) -> List[MatterModel]:
        """Fetch recent Clio matters."""
        response = self.api.matter_index(limit=limit)
        raw_matters = response.data

        matters = []
        for item in raw_matters:
            matter = MatterModel(
                id=item.id,
                display_number=item.display_number,
                description=item.description,
                status=item.status,
                client_name=item.client.get('name') if item.client else None,
                practice_area=item.practice_area.get('name') if item.practice_area else None
            )
            matters.append(matter)


        return matters

def get_matter_by_id(self, matter_id: int) -> MatterModel:
    """Fetch a single matter by ID."""
    item = self.api.matter_show(matter_id).data

    return MatterModel(
        id=item.id,
        display_number=item.display_number,
        custom_number=item.custom_number,
        description=item.description,
        status=item.status,
        location=item.location,
        client_reference=item.client_reference,
        client_id=item.client.id if item.client else None,
        client_name=item.client.name if item.client else None,
        practice_area_name=item.practice_area.name if item.practice_area else None,
        billable=item.billable,
        open_date=item.open_date,
        close_date=item.close_date,
        pending_date=item.pending_date,
        created_at=item.created_at,
        updated_at=item.updated_at,
        shared=item.shared,
        has_tasks=item.has_tasks,
        last_activity_date=item.last_activity_date,
        matter_stage_updated_at=item.matter_stage_updated_at,
        currency=item.currency,
        matter_stage_id=item.matter_stage.id if item.matter_stage else None,
        matter_stage_name=item.matter_stage.name if item.matter_stage else None,
        maildrop_address=item.maildrop_address,
        billing_method=item.billing_method
    )

# Get matters by client ID
def get_matters_by_client_id(self, client_id: int) -> List[MatterModel]:
    """Fetch all matters associated with a specific client."""
    response = self.api.matter_index(client_id=client_id)
    raw_matters = response.data

    matters = []
    for item in raw_matters:
        matter = MatterModel(
            id=item.id,
            display_number=item.display_number,
            custom_number=item.custom_number,
            description=item.description,
            status=item.status,
            location=item.location,
            client_reference=item.client_reference,
            client_id=item.client.id if item.client else None,
            client_name=item.client.name if item.client else None,
            practice_area_name=item.practice_area.name if item.practice_area else None,
            billable=item.billable,
            open_date=item.open_date,
            close_date=item.close_date,
            pending_date=item.pending_date,
            created_at=item.created_at,
            updated_at=item.updated_at,
            shared=item.shared,
            has_tasks=item.has_tasks,
            last_activity_date=item.last_activity_date,
            matter_stage_updated_at=item.matter_stage_updated_at,
            currency=item.currency,
            matter_stage_id=item.matter_stage.id if item.matter_stage else None,
            matter_stage_name=item.matter_stage.name if item.matter_stage else None,
            maildrop_address=item.maildrop_address,
            billing_method=item.billing_method
        )
        matters.append(matter)

    return matters
