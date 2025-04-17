from firm_core.custom_models.activity import ActivityModel
from clio_sdk.models.activity import Activity as ClioActivity
from clio_sdk.models.activity_create_request import ActivityCreateRequest
from clio_sdk.models.activity_update_request import ActivityUpdateRequest

class ActivityMapper:
    @staticmethod
    def from_clio(clio_obj: ClioActivity) -> ActivityModel:
        activity = clio_obj.activity
        return ActivityModel(
            
            id=getattr(activity, "id", None),
            
            source=getattr(activity, "source", None),
            
            external_id=getattr(activity, "external_id", None),
            
            date=getattr(activity, "date", None),
            
            description=getattr(activity, "description", None),
            
            amount=getattr(activity, "amount", None),
            
            quantity=getattr(activity, "quantity", None),
            
            rate=getattr(activity, "rate", None),
            
            matter_id=getattr(activity, "matter_id", None),
            
            contact_id=getattr(activity, "contact_id", None),
            
            contact_name=getattr(activity, "contact_name", None),
            
            type=getattr(activity, "type", None),
            
        )

    @staticmethod
    def to_sdk_create(activity: ActivityModel) -> ActivityCreateRequest:
        return ActivityCreateRequest(
            activity={
                
                "id": activity.id,
                
                "source": activity.source,
                
                "external_id": activity.external_id,
                
                "date": activity.date,
                
                "description": activity.description,
                
                "amount": activity.amount,
                
                "quantity": activity.quantity,
                
                "rate": activity.rate,
                
                "matter_id": activity.matter_id,
                
                "contact_id": activity.contact_id,
                
                "contact_name": activity.contact_name,
                
                "type": activity.type,
                
            }
        )

    @staticmethod
    def to_sdk_update(activity: ActivityModel) -> ActivityUpdateRequest:
        return ActivityUpdateRequest(
            activity={
                
                "id": activity.id,
                
                "source": activity.source,
                
                "external_id": activity.external_id,
                
                "date": activity.date,
                
                "description": activity.description,
                
                "amount": activity.amount,
                
                "quantity": activity.quantity,
                
                "rate": activity.rate,
                
                "matter_id": activity.matter_id,
                
                "contact_id": activity.contact_id,
                
                "contact_name": activity.contact_name,
                
                "type": activity.type,
                
            }
        )