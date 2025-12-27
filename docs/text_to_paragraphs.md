# Converting document into paragraphs

Many experimental protocols, synthesis descriptions and scientific reports are distributed as HTML/pdf/xml files.
Before these texts can be used for **paragraph-level classification** (e.g. identifying synthetic conditions) they must be converted into clean well-defined paragraph units. The reason for this is because most llm have a maximum amount of tokens that can be processed. Therefore, it is important to split into paragraphs before to identify synthetic paragraphs from which synthetic conditions can be extracted.

`synthetic_paragraph_classifier` provides a simple and reliable pipeline for:

1. Converting HTMLPDF/XML documents into plain text
2. Splitting the text into paragraph-level units suitable for NLP and LLM fine-tuning

---

## html files to list of paragraphs

The fillowing lines of codes can be used to quickly convert
an html file to a list of paragaraphs.

```Python
from synthetic_paragraph_classifier.process_doc.convert_html_to_text import html_2_text

from synthetic_paragraph_classifier.process_doc.doc_parser import text_2_paragraphs

# path to html file
html_path = "data/html/MALRAU.html"

# convert html files to plaintext
plain_text = html_2_text(html_path)

# list of paragraphs
paragraphs = text_2_paragraphs(plain_text)
```

## PDF files to list of paragraphs

The fillowing lines of codes can be used to quickly convert
a pdf file to a list of paragaraphs.

```Python
from synthetic_paragraph_classifier.process_doc.convert_html_to_text import convert_pdf_to_plaintext

from synthetic_paragraph_classifier.process_doc.doc_parser import text_2_paragraphs

# path to html file
pdf_path = "data/pdf/dinga.pdf"

# convert html files to plaintext
plain_text = convert_pdf_to_plaintext(pdf_path)

# list of paragraphs
paragraphs = text_2_paragraphs(plain_text)
```

This list of paragraphs can now be parsed to the classifier to
identify and return pagraphs describing synthetic protocols.