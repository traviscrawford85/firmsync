from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH


def apply_document_styles(document, style_config):
    for paragraph in document.paragraphs:
        if paragraph.style and hasattr(paragraph.style, 'font'):
            font = paragraph.style.font
            font.name = style_config.get("font_name", "Times New Roman")
            font.size = Pt(style_config.get("font_size", 12))

        paragraph_format = paragraph.paragraph_format
        paragraph_format.line_spacing = style_config.get("line_spacing", 1.15)
        paragraph_format.space_after = Pt(style_config.get("paragraph_spacing", 12))

        alignment = style_config.get("alignment", "left").lower()
        if alignment == "center":
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif alignment == "right":
            paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        else:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

    section = document.sections[0]
    section.top_margin = Inches(style_config.get("margin_top", 1))
    section.bottom_margin = Inches(style_config.get("margin_bottom", 1))
    section.left_margin = Inches(style_config.get("margin_left", 1))
    section.right_margin = Inches(style_config.get("margin_right", 1))
