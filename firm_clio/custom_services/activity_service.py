# firm_clio/custom_services/activity_service.py

from clio_sdk.api.activities_api import ActivitiesApi
from clio_sdk import ApiClient
from firm_clio.mappers.activity_mapper import clio_activity_to_model
from firm_core.custom_models.activity import ActivityModel
from firm_clio.clio_client import get_clio_client


class ActivityService:
    def __init__(self):
        client: ApiClient = get_clio_client()
        self.api = ActivitiesApi(client)

    def get_recent_activities(self, limit: int = 10) -> list[ActivityModel]:
        """
        Fetch recent Clio activities and return them as ActivityModel instances.
        """
        raw_response = self.api.list_activities(per_page=limit)
        raw_activities = raw_response.get("data", [])

        print(f"🧾 Retrieved {len(raw_activities)} Clio activities")

        return [clio_activity_to_model(activity) for activity in raw_activities]

    def get_activity_by_id(self, activity_id: str) -> ActivityModel:
        """
        Fetch a single Clio activity by ID and return as ActivityModel.
        """
        activity_data = self.api.get_activity(activity_id)
        return clio_activity_to_model(activity_data["data"])
