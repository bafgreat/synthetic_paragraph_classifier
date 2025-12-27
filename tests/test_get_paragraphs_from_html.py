
import os
import pytest

from synthetic_paragraph_classifier.process_doc.convert_html_to_text import (
    html_2_text,
    html_2_text2,
)
from synthetic_paragraph_classifier.process_doc.doc_parser import text_2_paragraphs


@pytest.fixture(scope="module")
def html_file_path():
    """
    Fixture providing the path to the test HTML file.
    Ensures the file exists before running tests.
    """
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "html",
        "MALRAU.html",
    )
    assert os.path.isfile(path), f"Test HTML file not found: {path}"
    return path


def test_html_2_text2_section_count(html_file_path):
    """
    Test that html_2_text2 correctly extracts the expected
    number of sections from the HTML file.
    """
    sections = html_2_text2(html_file_path)
    assert len(sections) == 114


def test_html_2_text_and_paragraph_count(html_file_path):
    """
    Test that html_2_text produces plain text that is correctly
    split into the expected number of paragraphs.
    """
    plain_text = html_2_text(html_file_path)
    paragraphs = text_2_paragraphs(plain_text)

    assert len(paragraphs) == 358
