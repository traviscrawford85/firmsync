# clio_utils.py

from typing import Any
from pprint import pprint
from datetime import datetime, date
from pydantic import BaseModel

# This module provides utility functions for inspecting and dumping Pydantic models.
# It includes functions to inspect model instances, list model fields, and dump models as JSON.


def inspect_model_instance(model_instance: Any):
    print(
        f"\n📦 Inspecting model instance: {model_instance.__class__.__name__}")
    for field, value in model_instance.model_dump().items():
        print(f"  {field}: {value}")


def list_model_fields(model_class: Any):
    print(f"\n🧬 Fields in model: {model_class.__name__}")
    for field, definition in model_class.model_fields.items():
        print(f"  {field}: {definition.annotation}")


def dump_model_as_json(model_instance: Any):
    print(f"\n🗃️ JSON Dump of {model_instance.__class__.__name__}")
    print(model_instance.model_dump_json(indent=2))


def list_testable_fields(model_class: Any):
    return list(model_class.model_fields.keys())


def generate_display_number(year: int, matter_id: int, first_name: str, last_name: str) -> str:
    padded_id = str(matter_id).zfill(5)  # Pad to 5 digits
    return f"{year}-{padded_id} {last_name},{first_name}"


def inspect_field(model_instance, field_path):
    """
    Inspect a nested field within a model using dot notation (e.g., 'client.name').
    """
    try:
        current = model_instance
        for key in field_path.split("."):
            current = getattr(current, key)
        print(f"🔍 Value at '{field_path}':")
        if hasattr(current, 'model_dump'):
            from pprint import pprint
            pprint(current.model_dump())
        else:
            print(current)
    except AttributeError:
        print(f"❌ Field '{field_path}' not found.")

# validate_required_fields function checks if the required fields are present in the data dictionary.


def validate_required_fields(data: dict, required_fields: list, context: str = "unknown") -> bool:
    missing = [
        key for key in required_fields if key not in data or data[key] is None]
    if missing:
        print(f"❌ Missing required fields in {context} response: {missing}")
        return False
    print(f"✅ All required fields present in {context} response.")
    return True


def extract_custom_fields(custom_field_values: list) -> dict:
    """
    Converts Clio's list of custom fields into a name -> value dictionary.
    Handles nested structure safely.
    """
    if not custom_field_values:
        return {}

    field_map = {}
    for field in custom_field_values:
        name = field.get("name") or (
            field.get("custom_field") or {}).get("name")
        value = field.get("value")
        if name:
            field_map[name] = value
    return field_map


def to_dict(obj: Any) -> Any:
    if isinstance(obj, BaseModel):
        return to_dict(obj.model_dump())
    elif isinstance(obj, list):
        return [to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: to_dict(v) for k, v in obj.items()}
    return obj


def normalize_practice_area_id(data: dict):
    """Ensure that practice_area_id inside matter_stage is a string."""
    matter_stages = data.get("matter_stage")
    if isinstance(matter_stages, list):
        for stage in matter_stages:
            if isinstance(stage, dict):
                if "practice_area_id" in stage and isinstance(stage["practice_area_id"], int):
                    print(
                        f"🔧 Converting practice_area_id from int → str: {stage['practice_area_id']}")
                    stage["practice_area_id"] = str(stage["practice_area_id"])
