from typing import List, Generator
from clio_sdk.api.matters_api import MattersApi
from firm_clio.clio_client import get_clio_client
from firm_clio.custom_models.matter import MatterModel
from firm_clio.custom_services.paginated_service import PaginatedService


class MatterService(PaginatedService):
    def __init__(self):
        self.client = get_clio_client()
        self.api = MattersApi(self.client)

    def get_matter_by_id(self, matter_id: int) -> MatterModel:
        item = self.api.matter_show(matter_id).data
        return self._parse_matter(item)

    def get_recent_matters(self, limit: int = 10) -> List[MatterModel]:
        response = self.api.matter_index(limit=limit).data
        return [self._parse_matter(item) for item in response]

    def get_matters_by_client_id(self, client_id: int) -> List[MatterModel]:
        response = self.api.matter_index(client_id=client_id).data
        return [self._parse_matter(item) for item in response]

    def get_all_matters(self) -> List[MatterModel]:
        return [self._parse_matter(item) for item in self.paginate(self.api.matter_index)]

    def yield_matters(self) -> Generator[MatterModel, None, None]:
        for item in self.paginate(self.api.matter_index):
            yield self._parse_matter(item)

    def _parse_matter(self, item) -> MatterModel:
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
