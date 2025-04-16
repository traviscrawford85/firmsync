import yaml
import re
from docx import Document


def load_schema(schema_path):
    with open(schema_path, "r") as file:
        return yaml.safe_load(file)


def extract_merge_fields(document: Document):
    pattern = re.compile(r"<<(.*?)>>")
    fields = set()

    for paragraph in document.paragraphs:
        matches = pattern.findall(paragraph.text)
        fields.update(matches)

    # Optional: Also scan tables
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                matches = pattern.findall(cell.text)
                fields.update(matches)

    return fields
