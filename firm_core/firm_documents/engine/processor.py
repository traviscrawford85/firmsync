from docx import Document
from pathlib import Path
import yaml

from .schema_utils import extract_merge_fields, load_schema
from .style_utils import apply_document_styles


class DocumentTemplateProcessor:
    def __init__(self, template_path: Path, schema_path: Path, style_path: Path):
        self.template_path = Path(template_path)
        self.schema_path = Path(schema_path)
        self.style_path = Path(style_path)

        self.document = self._load_document()
        self.schema = self._load_schema()
        self.style_config = self._load_styles()

    def _load_document(self):
        if not self.template_path.exists():
            raise FileNotFoundError(f"Template not found: {self.template_path}")
        return Document(self.template_path)

    def _load_schema(self):
        return load_schema(self.schema_path)

    def _load_styles(self):
        if not self.style_path.exists():
            raise FileNotFoundError(f"Style config not found: {self.style_path}")
        with open(self.style_path, "r") as f:
            return yaml.safe_load(f)

    def apply_styles(self):
        apply_document_styles(self.document, self.style_config)

    def validate_merge_fields(self):
        actual_fields = extract_merge_fields(self.document)
        required_fields = set(self.schema.get("required_fields", []))
        return required_fields - actual_fields

    def save(self, output_path: Path):
        output_path.parent.mkdir(parents=True, exist_ok=True)
        self.document.save(output_path)
