import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import sys


def generate_model(json_path: str):
    with open(json_path, "r") as f:
        config = json.load(f)

    model_name = config["model"]
    fields = config.get("fields", [])
    related_models = config.get("related_models", [])
    description = config.get("description", "")

    env = Environment(loader=FileSystemLoader("templates"))

    # Generate model
    model_template = env.get_template("model_template.jinja2")
    model_rendered = model_template.render(
        model_name=model_name,
        fields=fields,
        related_models=related_models,
        description=description
    )
    model_output_path = Path("firm_core/custom_models") / \
        f"{model_name.lower()}.py"
    model_output_path.parent.mkdir(parents=True, exist_ok=True)
    model_output_path.write_text(model_rendered)
    print(f"✅ Model generated at: {model_output_path}")

    # Generate mapper
    mapper_template = env.get_template("mapper_template.jinja2")
    mapper_rendered = mapper_template.render(
        model_name=model_name,
        fields=fields,
        related_models=related_models
    )
    mapper_output_path = Path("firm_clio/mappers") / \
        f"{model_name.lower()}_mapper.py"
    mapper_output_path.parent.mkdir(parents=True, exist_ok=True)
    mapper_output_path.write_text(mapper_rendered)
    print(f"✅ Mapper generated at: {mapper_output_path}")


if __name__ == "__main__":
    path = sys.argv[1] if len(
        sys.argv) > 1 else "firm_core/config/activity_composite_model.json"
    generate_model(path)
