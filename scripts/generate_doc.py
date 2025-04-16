import sys
from pathlib import Path

# Dynamically add the project's root directory to sys.path
current_file = Path(__file__).resolve()
project_root = current_file.parents[2]  # Assumes this file is 3 levels deep
sys.path.insert(0, str(project_root))

from firm_core.firm_documents.engine.processor import DocumentTemplateProcessor

# Base project directory (e.g., E:/Projects/firmsync)
BASE_DIR = project_root

def generate_pip_letter():
    processor = DocumentTemplateProcessor(
        template_path=BASE_DIR / "firmsync" / "firm_core" / "firm_documents" / "templates" / "letters" / "pip_letter_of_representation.docx",
        schema_path=BASE_DIR / "firmsync" / "firm_core" / "firm_documents" / "schemas" / "pip_letter_of_representation.yaml",
        style_path=BASE_DIR / "firmsync" / "firm_core" / "firm_documents" / "styles" / "styles.yaml"
    )

    missing_fields = processor.validate_merge_fields()

    if missing_fields:
        print("⚠️ Missing required merge fields:", missing_fields)
    else:
        print("✅ All merge fields present.")

    processor.apply_styles()

    # Save a test-rendered version locally
    output_path = BASE_DIR / "output" / "pip_letter_output.docx"
    processor.save(output_path)

    # Deploy to Clio template drive
    deployment_path = Path("A:/() Templates/My Firm's Templates/letters/pip_letter_of_representation.docx")
    processor.save(deployment_path)

if __name__ == "__main__":
    generate_pip_letter()
    print("PIP Letter of Representation generated and deployed successfully.")
