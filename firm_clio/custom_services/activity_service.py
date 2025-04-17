# firm_clio/custom_services/activity_service.py

from firm_clio.mappers.activity_mapper import ActivityMapper
from firm_core.custom_models.activity import ActivityModel
from clio_sdk.api.activities_api import ActivitiesApi
from clio_sdk.models.activity_create_request import ActivityCreateRequest
from clio_sdk.models.activity_update_request import ActivityUpdateRequest
from typing import List


class ActivityService:
    def __init__(self, sdk_api: ActivitiesApi):
        self.sdk = sdk_api

    def get_recent_activities(self, limit: int = 10) -> List[ActivityModel]:
        sdk_list = self.sdk.activity_index(limit=limit)
        return [ActivityMapper.from_clio(a) for a in sdk_list.data]

    def create_activity(self, activity: ActivityModel) -> ActivityModel:
        sdk_request = self._to_sdk_create(activity)
        sdk_response = self.sdk.activity_create(activity_create_request=sdk_request)
        return ActivityMapper.from_clio(sdk_response.data)

    def update_activity(self, activity_id: str, activity: ActivityModel) -> ActivityModel:
        sdk_request = self._to_sdk_update(activity)
        sdk_response = self.sdk.activity_update(id=int(activity_id), activity_update_request=sdk_request)
        return ActivityMapper.from_clio(sdk_response.data)

    def get_activity_by_id(self, activity_id: str) -> ActivityModel:
        sdk_response = self.sdk.activity_show(id=int(activity_id))
        return ActivityMapper.from_clio(sdk_response.data)

    def _to_sdk_create(self, activity: ActivityModel) -> ActivityCreateRequest:
        return ActivityCreateRequest(
            activity={
                "date": activity.date.isoformat(),
                "description": activity.description,
                "price": activity.amount,
                "quantity": activity.quantity,
                "rate": activity.rate,
                "matter_id": activity.matter_id,
                "contact_id": activity.contact_id,
                "type": activity.type
            }
        )

    def _to_sdk_update(self, activity: ActivityModel) -> ActivityUpdateRequest:
        return ActivityUpdateRequest(
            activity={
                "date": activity.date.isoformat(),
                "description": activity.description,
                "price": activity.amount,
                "quantity": activity.quantity,
                "rate": activity.rate,
                "matter_id": activity.matter_id,
                "contact_id": activity.contact_id,
                "type": activity.type
            }
        )
