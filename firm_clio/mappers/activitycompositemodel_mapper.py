from firm_core.custom_models.activity import 
from clio_sdk.models.activity import Activity as ClioActivity
from clio_sdk.models.activity_create_request import ActivityCreateRequest
from clio_sdk.models.activity_update_request import ActivityUpdateRequest

class Mapper:
    @staticmethod
    def from_clio(clio_obj: ) -> :
        return (
            id=str(clio_obj.id) if clio_obj.id else None,
            source="clio",
            external_id=str(clio_obj.id),
            date=clio_obj.date,
            description=clio_obj.description,
            amount=float(clio_obj.price or 0),
            quantity=clio_obj.quantity,
            rate=clio_obj.rate,
            matter_id=str(clio_obj.matter_id) if clio_obj.matter_id else None,
            contact_id=str(clio_obj.contact_id) if clio_obj.contact_id else None,
            contact_name=getattr(clio_obj, "contact_name", None),
            type=clio_obj.type
        )


    @staticmethod
    def to_sdk_create(activity: ) -> ActivityCreateRequest:
        return ActivityCreateRequest(
            activity={
                
                "id": activity.id,
                
                "external_id": activity.external_id,
                
                "source": activity.source,
                
                "date": activity.date,
                
                "description": activity.description,
                
                "amount": activity.amount,
                
                "quantity": activity.quantity,
                
                "rate": activity.rate,
                
                "type": activity.type,
                
                "matter_id": activity.matter_id,
                
                "contact_id": activity.contact_id,
                
                "contact_name": activity.contact_name,
                
                "qbo_vendor_id": activity.qbo_vendor_id,
                
                "qbo_account_id": activity.qbo_account_id,
                
                "qbo_item_id": activity.qbo_item_id,
                
                "qbo_customer_id": activity.qbo_customer_id,
                
                "qbo_synced_at": activity.qbo_synced_at,
                
                "status": activity.status,
                
            }
        )

    @staticmethod
    def to_sdk_update(activity: ) -> ActivityUpdateRequest:
        return ActivityUpdateRequest(
            activity={
                
                "id": activity.id,
                
                "external_id": activity.external_id,
                
                "source": activity.source,
                
                "date": activity.date,
                
                "description": activity.description,
                
                "amount": activity.amount,
                
                "quantity": activity.quantity,
                
                "rate": activity.rate,
                
                "type": activity.type,
                
                "matter_id": activity.matter_id,
                
                "contact_id": activity.contact_id,
                
                "contact_name": activity.contact_name,
                
                "qbo_vendor_id": activity.qbo_vendor_id,
                
                "qbo_account_id": activity.qbo_account_id,
                
                "qbo_item_id": activity.qbo_item_id,
                
                "qbo_customer_id": activity.qbo_customer_id,
                
                "qbo_synced_at": activity.qbo_synced_at,
                
                "status": activity.status,
                
            }
        )