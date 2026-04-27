from typing import List, Dict, Optional
import bs4
from bs4 import BeautifulSoup
import re
from collections import defaultdict


SUBSTITUTE_TAGS = {
    'persName',
    'orgName',
    'publicationStmt',
    'titleStmt',
    'biblScope'
}


def clean_tags(el: bs4.element.Tag):
    """
    Replace all tags with lowercase version
    :param el:
    :return:
    """
    pass


def soup_from_path(file_path: str):
    """
    Read XML file
    :param file_path:
    :return:
    """
    pass


def get_title_from_grobid_xml(raw_xml: BeautifulSoup) -> str:
    """
    Returns title
    :return:
    """
    pass


def get_author_names_from_grobid_xml(raw_xml: BeautifulSoup) -> List[Dict[str, str]]:
    """
    Returns a list of dictionaries, one for each author,
    containing the first and last names.

    e.g.
        {
            "first": first,
            "middle": middle,
            "last": last,
            "suffix": suffix
        }
    """
    pass


def get_affiliation_from_grobid_xml(raw_xml: BeautifulSoup) -> Dict:
    """
    Get affiliation from grobid xml
    :param raw_xml:
    :return:
    """
    pass


def get_author_data_from_grobid_xml(raw_xml: BeautifulSoup) -> List[Dict]:
    """
    Returns a list of dictionaries, one for each author,
    containing the first and last names.

    e.g.
        {
            "first": first,
            "middle": middle,
            "last": last,
            "suffix": suffix,
            "affiliation": {
                "laboratory": "",
                "institution": "",
                "location": "",
            },
            "email": ""
        }
    """
    pass


def get_year_from_grobid_xml(raw_xml: BeautifulSoup) -> Optional[int]:
    """
    Returns date published if exists
    :return:
    """
    pass


def get_venue_from_grobid_xml(raw_xml: BeautifulSoup, title_text: str) -> str:
    """
    Returns venue/journal/publisher of bib entry
    Grobid ref documentation: https://grobid.readthedocs.io/en/latest/training/Bibliographical-references/
    level="j": journal title
    level="m": "non journal bibliographical item holding the cited article"
    level="s": series title
    :return:
    """
    pass


def get_volume_from_grobid_xml(raw_xml: BeautifulSoup) -> str:
    """
    Returns the volume number of grobid bib entry
    Grobid <biblscope unit="volume">
    :return:
    """
    pass


def get_issue_from_grobid_xml(raw_xml: BeautifulSoup) -> str:
    """
    Returns the issue number of grobid bib entry
    Grobid <biblscope unit="issue">
    :return:
    """
    pass


def get_pages_from_grobid_xml(raw_xml: BeautifulSoup) -> str:
    """
    Returns the page numbers of grobid bib entry
    Grobid <biblscope unit="page">
    :return:
    """
    pass


def get_other_ids_from_grobid_xml(raw_xml: BeautifulSoup) -> Dict[str, List]:
    """
    Returns a dictionary of other identifiers from grobid bib entry (arxiv, pubmed, doi)
    :param raw_xml:
    :return:
    """
    pass


def get_raw_bib_text_from_grobid_xml(raw_xml: BeautifulSoup) -> str:
    """
    Returns the raw bibiliography string
    :param raw_xml:
    :return:
    """
    pass


def get_publication_datetime_from_grobid_xml(raw_xml: BeautifulSoup) -> str:
    """
    Finds and returns the publication datetime if it exists
    :param raw_xml:
    :return:
    """
    pass


def parse_bib_entry(bib_entry: BeautifulSoup) -> Dict:
    """
    Parse one bib entry
    :param bib_entry:
    :return:
    """
    pass


def is_reference_tag(tag: bs4.element.Tag) -> bool:
    pass


def extract_paper_metadata_from_grobid_xml(tag: bs4.element.Tag) -> Dict:
    """
    Extract paper metadata (title, authors, affiliation, year) from grobid xml
    :param tag:
    :return:
    """
    pass
