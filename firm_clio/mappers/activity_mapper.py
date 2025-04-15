# firm_clio/mappers/activity_mapper.py

from firm_core.custom_models.activity import ActivityModel


def clio_activity_to_model(activity: dict) -> ActivityModel:
    """Convert a Clio API activity response to an internal ActivityModel."""
    return ActivityModel(
        id=activity.get("id"),
        source="clio",
        external_id=activity.get("id"),
        date=activity.get("date"),
        description=activity.get("description"),
        amount=float(activity.get("rate") or 0),
        quantity=float(activity.get("quantity") or 1),
        type=activity.get("type", "time"),
        contact_id=activity.get("client", {}).get("id"),
    )


def to_clio_activity(activity: ActivityModel) -> dict:
    """Convert an internal ActivityModel to a Clio-compatible dictionary."""
    return {
        "id": activity.external_id,
        "date": activity.date.isoformat(),
        "description": activity.description,
        "rate": str(activity.amount),
        "quantity": str(activity.quantity),
        "type": activity.type,
        "client": {"id": activity.contact_id},
    }
