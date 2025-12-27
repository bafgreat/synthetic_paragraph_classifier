
import os
import pytest

from synthetic_paragraph_classifier.process_doc.convert_html_to_text import (
    convert_pdf_to_plaintext
)
from synthetic_paragraph_classifier.process_doc.doc_parser import text_2_paragraphs

@pytest.fixture(scope="module")
def pdf_file_path():
    """
    Fixture providing the path to the test HTML file.
    Ensures the file exists before running tests.
    """
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "pdf",
        "dinga.pdf",
    )
    assert os.path.isfile(path), f"Test pdf file not found: {path}"
    return path



def test_pdf_2_text_and_paragraph_count(pdf_file_path):
    """
    Test that html_2_text produces plain text that is correctly
    split into the expected number of paragraphs.
    """
    plain_text = convert_pdf_to_plaintext(pdf_file_path)
    paragraphs = text_2_paragraphs(plain_text)

    assert len(paragraphs) == 1164
