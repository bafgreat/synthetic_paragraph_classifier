#!/usr/bin/python
from __future__ import print_function
__author__ = "Dr. Dinga Wonanke"
__status__ = "production"
import inscriptis
import fitz
import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
# from pdfdataextractor import Reader


def find_xml_namespace(markup_file, name_pattern):
    """
    a simple function to find xml name space
    """
    namespace = {}
    all_name_list = []
    if type(name_pattern) == str:
        all_name_list.append(name_pattern)
    elif type(name_pattern) == list:
        all_name_list.extend(name_pattern)

    with open(markup_file, 'r', encoding="utf-8") as file_object:
        file_object = file_object.read()
        for n_pattern in all_name_list:
            pattern = r'xmlns:'+n_pattern+r'[^\s]+'
            match = re.search(pattern, file_object)
            if match:
                found_name_space = re.search(
                    r'"(.*?)"',  match.group()).group(1)
                namespace[n_pattern] = found_name_space
    return namespace


def html_2_text(html_file):
    """
    A function that uses inscriptis to convert
    html files to plain text.
    Parameters
    ----------
    html_file: html file name or path: str.type

    Returns
    -------
    plain text : str.type
    """
    with open(html_file, 'r', encoding="utf-8") as file_object:
        html_object = file_object.read()

    return inscriptis.get_text(html_object)


def html_2_text2(markup_file):
    """
    A function that uses inscriptis to convert
    html files to plain text.
    Parameters
    ----------
    html_file: html file name or path: str.type

    Returns
    -------
    plain text : str.type
    """

    # with open(html_file, 'r', encoding="utf-8") as file_object:
    #     html_object = file_object.read()
    # # headings = []
    # # Parse the HTML content with BeautifulSoup
    # soup = BeautifulSoup(html_object, 'html.parser')
    # # for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5']):
    # #     headings.append(heading.text.strip())

    # # Remove unwanted elements from the HTML document

    # for element in soup(['figure', 'figcaption', 'meta', 'author', 'affiliation', 'abstract',
    #                      'cite', 'table', 'references', 'acronym']):
    #     element.extract()

    # # Extract the text from the modified HTML document
    # text = inscriptis.get_text(str(soup))
    # return text

    text = []
    ext = markup_file[markup_file.rindex('.')+1:]
    if ext == 'html':
        with open(markup_file, 'r', encoding="utf-8") as file_object:
            file_object = file_object.read()
        soup = BeautifulSoup(file_object, 'html.parser')
        extract = soup(['title', 'h2', 'h1', 'h3', 'h4', 'p'])
        for element in extract:
            text.append(inscriptis.get_text(str(element)).strip())
    elif ext == 'xml':
        with open(markup_file, 'r', encoding="utf-8") as file_object:
            file_object = file_object.read()
        soup = BeautifulSoup(file_object, 'xml')
        extract = soup(['para', 'section-title'])
        for element in extract:
            text.append(inscriptis.get_text(str(element)))
    elif ext == 'pdf':
        text = convert_pdf_to_plaintext(markup_file)
    return text


def convert_pdf_to_plaintext(pdf_path: str) -> str:
    """
    Convert a PDF file to plain text using PyMuPDF.

    Parameters
    ----------
    pdf_path : str
        Path to the PDF file.

    Returns
    -------
    str
        Extracted plain text.
    """
    pages_text = []

    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text("text") or ""
            pages_text.append(text)

    text = "\n\n".join(pages_text)


    text = text.replace("\r\n", "\n").replace("\r", "\n")


    text = re.sub(r"[ \t]+\n", "\n", text)

    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # --- Key part for your regex ---
    # Indent each paragraph (except maybe the very first) with two spaces
    # so your pattern r"(\n{2,}|\n)(\t|\s{2,}).*?" will match.
    paragraphs = text.split("\n\n")
    paragraphs = [p.strip() for p in paragraphs if p.strip()]

    # Add 2-space indent to every paragraph line block
    indented = ["  " + p.replace("\n", "\n  ") for p in paragraphs]

    # Join back with *single* newline between paragraphs (either is fine),
    # but your regex triggers on \n or \n\n anyway.
    return "\n\n".join(indented)
