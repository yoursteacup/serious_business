from docxtpl import DocxTemplate
from docx import Document
from datetime import datetime
import os

from validation_models import ordering


def generate(data):
    merged_doc = Document()

    for i, (path, class_name) in enumerate(ordering.items()):
        valid_data = class_name(**data[i])

        template = DocxTemplate(f"templates/{path}")
        template.render(data[i])
        template.save(f"docs_gen/temp_{i}.docx")
        doc = Document(f"docs_gen/temp_{i}.docx")

        for element in doc.element.body:
            merged_doc.element.body.append(element)

        os.remove(f"docs_gen/temp_{i}.docx")

    merged_doc.save(f"docs_gen/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.docx")
