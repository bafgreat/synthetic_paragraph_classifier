# synthetic_paragraph_classifier

**synthetic_paragraph_classifier** is a Python module for
predicting paragraphs containing synthetic protocols in
manuscripts. The idea is that **LLMs** do have a maximum
token counts thus it is essential to extract only relevant
paragraphs for extracting synthetic conditions.

The module can work on both **html** and **pdf** files.

## Intallation

The installation can be done via **git** or **PyPI**.

### Git Installation

To install using git simply clone the repository and install using
the following codes.

```Bash

git clone https://github.com/bafgreat/synthetic_paragraph_classifier.git

cd synthetic_paragraph_classifier

pip install .
```

### PYPI Installation

To install via PYPI simply run the following code.

```Bash

pip install synthetic_paragraph_classifier
```

## Usage

The easiest way to use this code is as follows.

### Convert HTML or PDF to list of paragraphs

To convert an html or a pdf file to list of paragraphs,
run the following lines of codes.

```Bash

from synthetic_paragraph_classifier.process_doc.convert_html_to_text import html_2_text, convert_pdf_to_plaintext

from synthetic_paragraph_classifier.process_doc.doc_parser import text_2_paragraphs

# Convert html to list of paragraphs
html_path = "data/html/MALRAU.html"
plain_text = html_2_text(html_path)
paragraphs = text_2_paragraphs(plain_text)

# Covert pdf to list of paragraphs
pdf_path = "data/pdf/dinga.pdf"
plain_text = convert_pdf_to_plaintext(pdf_path)
paragraphs = text_2_paragraphs(plain_text)

```








# LICENSE

MIT license 