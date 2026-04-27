#!/usr/bin/env python

import os
import sys
import bs4
import re
from bs4 import BeautifulSoup, NavigableString
from typing import List, Dict, Tuple

from doc2json.s2orc import Paper

from doc2json.utils.grobid_util import parse_bib_entry, extract_paper_metadata_from_grobid_xml
from doc2json.utils.citation_util import SINGLE_BRACKET_REGEX, BRACKET_REGEX, BRACKET_STYLE_THRESHOLD
from doc2json.utils.citation_util import is_expansion_string, _clean_empty_and_duplicate_authors_from_grobid_parse
from doc2json.utils.refspan_util import sub_spans_and_update_indices


REPLACE_TABLE_TOKS = {
    "<row>": "<tr>",
    "<row/>": "<tr/>",
    "</row>": "</tr>",
    "<cell>": "<td>",
    "<cell/>": "<td/>",
    "</cell>": "</td>",
    "<cell ": "<td ",
    "cols=": "colspan="
}


class UniqTokenGenerator:
    """
    Generate unique token
    """
    def __init__(self, tok_string):
        self.tok_string = tok_string
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        pass


def normalize_grobid_id(grobid_id: str):
    """
    Normalize grobid object identifiers
    :param grobid_id:
    :return:
    """
    pass


def parse_bibliography(soup: BeautifulSoup) -> List[Dict]:
    """
    Finds all bibliography entries in a grobid xml.
    """
    pass


def extract_formulas_from_tei_xml(sp: BeautifulSoup) -> None:
    """
    Replace all formulas with the text
    :param sp:
    :return:
    """
    pass


def table_to_html(table: bs4.element.Tag) -> str:
    """
    Sub table tags with html table tags
    :param table_str:
    :return:
    """
    pass


def extract_figures_and_tables_from_tei_xml(sp: BeautifulSoup) -> Dict[str, Dict]:
    """
    Generate figure and table dicts
    :param sp:
    :return:
    """
    pass


def check_if_citations_are_bracket_style(sp: BeautifulSoup) -> bool:
    """
    Check if the document has bracket style citations
    :param sp:
    :return:
    """
    pass


def sub_all_note_tags(sp: BeautifulSoup) -> BeautifulSoup:
    """
    Sub all note tags with p tags
    :param para_el:
    :param sp:
    :return:
    """
    pass


def process_formulas_in_paragraph(para_el: BeautifulSoup, sp: BeautifulSoup) -> None:
    """
    Process all formulas in paragraph and replace with text and label
    :param para_el:
    :param sp:
    :return:
    """
    pass


def process_references_in_paragraph(para_el: BeautifulSoup, sp: BeautifulSoup, refs: Dict) -> Dict:
    """
    Process all references in paragraph and generate a dict that contains (type, ref_id, surface_form)
    :param para_el:
    :param sp:
    :param refs:
    :return:
    """
    pass


def process_citations_in_paragraph(para_el: BeautifulSoup, sp: BeautifulSoup, bibs: Dict, bracket: bool) -> Dict:
    """
    Process all citations in paragraph and generate a dict for surface forms
    :param para_el:
    :param sp:
    :param bibs:
    :param bracket:
    :return:
    """
    pass


def process_paragraph(
        sp: BeautifulSoup,
        para_el: bs4.element.Tag,
        section_names: List[Tuple],
        bib_dict: Dict,
        ref_dict: Dict,
        bracket: bool
) -> Dict:
    """
    Process one paragraph
    :param sp:
    :param para_el:
    :param section_names:
    :param bib_dict:
    :param ref_dict:
    :param bracket: if bracket style, expand and clean up citations
    :return:
    """
    pass


def extract_abstract_from_tei_xml(
        sp: BeautifulSoup,
        bib_dict: Dict,
        ref_dict: Dict,
        cleanup_bracket: bool
) -> List[Dict]:
    """
    Parse abstract from soup
    :param sp:
    :param bib_dict:
    :param ref_dict:
    :param cleanup_bracket:
    :return:
    """
    pass


def extract_body_text_from_div(
        sp: BeautifulSoup,
        div: bs4.element.Tag,
        sections: List[Tuple],
        bib_dict: Dict,
        ref_dict: Dict,
        cleanup_bracket: bool
) -> List[Dict]:
    """
    Parse body text from soup
    :param sp:
    :param div:
    :param sections:
    :param bib_dict:
    :param ref_dict:
    :param cleanup_bracket:
    :return:
    """
    pass


def extract_body_text_from_tei_xml(
        sp: BeautifulSoup,
        bib_dict: Dict,
        ref_dict: Dict,
        cleanup_bracket: bool
) -> List[Dict]:
    """
    Parse body text from soup
    :param sp:
    :param bib_dict:
    :param ref_dict:
    :param cleanup_bracket:
    :return:
    """
    pass


def extract_back_matter_from_tei_xml(
        sp: BeautifulSoup,
        bib_dict: Dict,
        ref_dict: Dict,
        cleanup_bracket: bool
) -> List[Dict]:
    """
    Parse back matter from soup
    :param sp:
    :param bib_dict:
    :param ref_dict:
    :param cleanup_bracket:
    :return:
    """
    pass


def convert_tei_xml_soup_to_s2orc_json(soup: BeautifulSoup, paper_id: str, pdf_hash: str) -> Paper:
    """
    Convert Grobid TEI XML to S2ORC json format
    :param soup: BeautifulSoup of XML file content
    :param paper_id: name of file
    :param pdf_hash: hash of PDF
    :return:
    """
    pass


def convert_tei_xml_file_to_s2orc_json(tei_file: str, pdf_hash: str = "") -> Paper:
    """
    Convert a TEI XML file to S2ORC JSON
    :param tei_file:
    :param pdf_hash:
    :return:
    """
    pass
