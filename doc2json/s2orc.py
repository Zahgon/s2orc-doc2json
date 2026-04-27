"""
S2ORC classes
"""

from datetime import datetime
from typing import Dict, List, Optional
from doc2json.config import *


CORRECT_KEYS = {
    "issn": "issue",
    "type": "type_str"
}

SKIP_KEYS = {
    'link',
    'bib_id'
}

REFERENCE_OUTPUT_KEYS = {
    'figure': {'text', 'type_str', 'uris', 'num', 'fig_num'},
    'table': {'text', 'type_str', 'content', 'num', 'html'},
    'footnote': {'text', 'type_str', 'num'},
    'section': {'text', 'type_str', 'num', 'parent'},
    'equation': {'text', 'type_str', 'latex', 'mathml', 'num'}
}

METADATA_KEYS = {
    "title", "authors", "year", "venue", "identifiers"
}


class ReferenceEntry:
    """
    Class for representing S2ORC figure and table references

    An example json representation (values are examples, not accurate):

    {
      "FIGREF0": {
        "text": "FIG. 2. Depth profiles of...",
        "latex": null,
        "type": "figure"
      },
      "TABREF2": {
        "text": "Diversity indices of...",
        "latex": null,
        "type": "table",
        "content": "",
        "html": ""
      }
    }
    """
    def __init__(
            self,
            ref_id: str,
            text: str,
            type_str: str,
            latex: Optional[str] = None,
            mathml: Optional[str] = None,
            content: Optional[str] = None,
            html: Optional[str] = None,
            uris: Optional[List[str]] = None,
            num: Optional[str] = None,
            parent: Optional[str] = None,
            fig_num: Optional[str] = None
    ):
        self.ref_id = ref_id
        self.text = text
        self.type_str = type_str
        self.latex = latex
        self.mathml = mathml
        self.content = content
        self.html = html
        self.uris = uris
        self.num = num
        self.parent = parent
        self.fig_num = fig_num

    def as_json(self):
        pass


class BibliographyEntry:
    """
    Class for representing S2ORC parsed bibliography entries

    An example json representation (values are examples, not accurate):

    {
        "title": "Mobility Reports...",
        "authors": [
            {
                "first": "A",
                "middle": ["A"],
                "last": "Haija",
                "suffix": ""
            }
        ],
        "year": 2015,
        "venue": "IEEE Wireless Commun. Mag",
        "volume": "42",
        "issn": "9",
        "pages": "80--92",
        "other_ids": {
            "doi": [
                "10.1109/TWC.2014.2360196"
            ],

        }
    }

    """
    def __init__(
            self,
            bib_id: str,
            title: str,
            authors: List[Dict[str, str]],
            ref_id: Optional[str] = None,
            year: Optional[int] = None,
            venue: Optional[str] = None,
            volume: Optional[str] = None,
            issue: Optional[str] = None,
            pages: Optional[str] = None,
            other_ids: Dict[str, List] = None,
            num: Optional[int] = None,
            urls: Optional[List] = None,
            raw_text: Optional[str] = None,
            links: Optional[List] = None
    ):
        self.bib_id = bib_id
        self.ref_id = ref_id
        self.title = title
        self.authors = authors
        self.year = year
        self.venue = venue
        self.volume = volume
        self.issue = issue
        self.pages = pages
        self.other_ids = other_ids
        self.num = num
        self.urls = urls
        self.raw_text = raw_text
        self.links = links

    def as_json(self):
        pass


class Affiliation:
    """
    Class for representing affiliation info

    Example:
        {
            "laboratory": "Key Laboratory of Urban Environment and Health",
            "institution": "Chinese Academy of Sciences",
            "location": {
              "postCode": "361021",
              "settlement": "Xiamen",
              "country": "People's Republic of China"
        }
    """
    def __init__(
            self,
            laboratory: str,
            institution: str,
            location: Dict
    ):
        self.laboratory = laboratory
        self.institution = institution
        self.location = location

    def as_json(self):
        pass


class Author:
    """
    Class for representing paper authors

    Example:

        {
          "first": "Anyi",
          "middle": [],
          "last": "Hu",
          "suffix": "",
          "affiliation": {
            "laboratory": "Key Laboratory of Urban Environment and Health",
            "institution": "Chinese Academy of Sciences",
            "location": {
              "postCode": "361021",
              "settlement": "Xiamen",
              "country": "People's Republic of China"
            }
          },
          "email": ""
        }
    """
    def __init__(
            self,
            first: str,
            middle: List[str],
            last: str,
            suffix: str,
            affiliation: Optional[Dict] = None,
            email: Optional[str] = None
    ):
        self.first = first
        self.middle = middle
        self.last = last
        self.suffix = suffix
        self.affiliation = Affiliation(**affiliation) if affiliation else {}
        self.email = email

    def as_json(self):
        pass


class Metadata:
    """
    Class for representing paper metadata

    Example:
    {
      "title": "Niche Partitioning...",
      "authors": [
        {
          "first": "Anyi",
          "middle": [],
          "last": "Hu",
          "suffix": "",
          "affiliation": {
            "laboratory": "Key Laboratory of Urban Environment and Health",
            "institution": "Chinese Academy of Sciences",
            "location": {
              "postCode": "361021",
              "settlement": "Xiamen",
              "country": "People's Republic of China"
            }
          },
          "email": ""
        }
      ],
      "year": "2011-11"
    }
    """
    def __init__(
            self,
            title: str,
            authors: List[Dict],
            year: Optional[str] = None,
            venue: Optional[str] = None,
            identifiers: Optional[Dict] = {}
    ):
        self.title = title
        self.authors = [Author(**author) for author in authors]
        self.year = year
        self.venue = venue
        self.identifiers = identifiers

    def as_json(self):
        pass


class Paragraph:
    """
    Class for representing a parsed paragraph from Grobid xml
    All xml tags are removed from the paragraph text, all figures, equations, and tables are replaced
    with a special token that maps to a reference identifier
    Citation mention spans and section header are extracted

    An example json representation (values are examples, not accurate):

    {
        "text": "Formal language techniques BID1 may be used to study FORMULA0 (see REF0)...",
        "mention_spans": [
            {
                "start": 27,
                "end": 31,
                "text": "[1]")
        ],
        "ref_spans": [
            {
                "start": ,
                "end": ,
                "text": "Fig. 1"
            }
        ],
        "eq_spans": [
            {
                "start": 53,
                "end": 61,
                "text": "Î± = 1",
                "latex": "\\alpha = 1",
                "ref_id": null
            }
        ],
        "section": "Abstract"
    }
    """
    def __init__(
            self,
            text: str,
            cite_spans: List[Dict],
            ref_spans: List[Dict],
            eq_spans: Optional[List[Dict]] = [],
            section: Optional = None,
            sec_num: Optional = None
    ):
        self.text = text
        self.cite_spans = cite_spans
        self.ref_spans = ref_spans
        self.eq_spans = eq_spans
        if type(section) == str:
            if section:
                sec_parts = section.split('::')
                section_list = [[None, sec_name] for sec_name in sec_parts]
            else:
                section_list = None
            if section_list and sec_num:
                section_list[-1][0] = sec_num
        else:
            section_list = section
        self.section = section_list

    def as_json(self):
        pass


class Paper:
    """
    Class for representing a parsed S2ORC paper
    """
    def __init__(
            self,
            paper_id: str,
            pdf_hash: str,
            metadata: Dict,
            abstract: List[Dict],
            body_text: List[Dict],
            back_matter: List[Dict],
            bib_entries: Dict,
            ref_entries: Dict
        ):
        self.paper_id = paper_id
        self.pdf_hash = pdf_hash
        self.metadata = Metadata(**metadata)
        self.abstract = [Paragraph(**para) for para in abstract]
        self.body_text = [Paragraph(**para) for para in body_text]
        self.back_matter = [Paragraph(**para) for para in back_matter]
        self.bib_entries = [
            BibliographyEntry(
                bib_id=key,
                **{CORRECT_KEYS[k] if k in CORRECT_KEYS else k: v for k, v in bib.items() if k not in SKIP_KEYS}
            ) for key, bib in bib_entries.items()
        ]
        self.ref_entries = [
            ReferenceEntry(
                ref_id=key,
                **{CORRECT_KEYS[k] if k in CORRECT_KEYS else k: v for k, v in ref.items() if k != 'ref_id'}
            ) for key, ref in ref_entries.items()
        ]

    def as_json(self):
        pass

    @property
    def raw_abstract_text(self) -> str:
        """
        Get all the body text joined by a newline
        :return:
        """
        pass

    @property
    def raw_body_text(self) -> str:
        """
        Get all the body text joined by a newline
        :return:
        """
        pass

    def release_json(self, doc_type: str="pdf"):
        """
        Return in release JSON format
        :return:
        """
        pass


def load_s2orc(paper_dict: Dict) -> Paper:
    """
    Load release S2ORC into Paper class
    :param paper_dict:
    :return:
    """
    pass
