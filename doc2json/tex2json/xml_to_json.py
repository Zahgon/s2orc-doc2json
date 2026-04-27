import os
import re
import itertools
import bs4
from bs4 import BeautifulSoup, NavigableString
from typing import List, Dict, Tuple, Optional
import copy
import latex2mathml.converter

from doc2json.grobid2json.grobid.grobid_client import GrobidClient
from doc2json.utils.grobid_util import parse_bib_entry, get_author_data_from_grobid_xml
from doc2json.s2orc import Paper, Paragraph


SKIP_TAGS = {
    'clearpage',
    'colorpool',
    'newpage',
    'tableofcontents'
}

TEXT_TAGS = {
    'p',
    'proof',
    'caption'
}


def normalize_latex_id(latex_id: str):
    pass


def process_author(
        author_text: str,
        grobid_client: GrobidClient,
        logfile: str
) -> List[Dict]:
    """
    Process authors
    :param author_text:
    :param grobid_client:
    :param logfile:
    :return:
    """
    pass


def process_bibentry(bib_text: str, grobid_client: GrobidClient, logfile: str):
    """
    Process one bib entry text into title, authors, etc
    :param bib_text:
    :param grobid_client:
    :param logfile:
    :return:
    """
    pass


def replace_ref_tokens(sp: BeautifulSoup, el: bs4.element.Tag, ref_map: Dict):
    """
    Replace all references in element with special tokens
    :param sp:
    :param el:
    :param ref_map:
    :return:
    """
    pass


def process_list_el(sp: BeautifulSoup, list_el: bs4.element.Tag, section_info: List, bib_map: Dict, ref_map: Dict):
    """
    Process list element
    :param sp:
    :param list_el:
    :param section_info:
    :param bib_map:
    :param ref_map:
    :return:
    """
    pass


def process_navstring(str_el: NavigableString, section_info: List):
    """
    Process one NavigableString
    :param sp:
    :param str_el:
    :param section_info:
    :param bib_map:
    :param ref_map:
    :return:
    """
    pass


def process_paragraph(sp: BeautifulSoup, para_el: bs4.element.Tag, section_info: List, bib_map: Dict, ref_map: Dict):
    """
    Process one paragraph
    :param sp:
    :param para_el:
    :param section_info:
    :param bib_map:
    :param ref_map:
    :return:
    """
    pass


def decompose_tags_before_title(sp: BeautifulSoup):
    """
    decompose all tags before title
    :param sp:
    :return:
    """
    pass


def process_metadata(sp: BeautifulSoup, grobid_client: GrobidClient, log_file: str) -> Tuple[str, List]:
    """
    Process metadata section in soup
    :param sp:
    :param grobid_client:
    :param log_file:
    :return:
    """
    pass


def process_bibliography_from_tex(sp: BeautifulSoup, client, log_file) -> Dict:
    """
    Parse bibliography from latex
    :return:
    """
    pass


def get_section_name(sec):
    """
    Get section name from div tag
    :param sec:
    :return:
    """
    pass


def get_sections_from_div(el: bs4.element.Tag, sp: BeautifulSoup, parent: Optional[str], faux_max: int) -> Dict:
    """
    Process section headers for one div
    :param el:
    :param sp:
    :return:
    """
    pass


def process_sections_from_text(sp: BeautifulSoup) -> Dict:
    """
    Generate section dict and replace with id tokens
    :param sp:
    :return:
    """
    pass


def process_equations_from_tex(sp: BeautifulSoup) -> Dict:
    """
    Generate equation dict and replace with id tokens
    :param sp:
    :return:
    """
    pass


def process_footnotes_from_text(sp: BeautifulSoup) -> Dict:
    """
    Process footnote marks
    :param sp:
    :return:
    """
    pass


def get_figure_map_from_tex(sp: BeautifulSoup) -> Dict:
    """
    Generate figure dict only
    :param sp:
    :return:
    """
    pass


def process_figures_from_tex(sp: BeautifulSoup, ref_map: Dict) -> Dict:
    """
    Add figure captions to fig_map and decompose
    :param sp:
    :param ref_map:
    :return:
    """
    pass


def convert_table_to_html(table_lst: List) -> str:
    pass


def extract_table(table: BeautifulSoup) -> List:
    """
    Extract table values from table entry
    :param table:
    :return:
    """
    pass


def get_table_map_from_text(sp: BeautifulSoup, keep_table_contents=True) -> Dict:
    """
    Generate table dict only
    :param sp:
    :param keep_table_contents:
    :return:
    """
    pass


def process_tables_from_tex(sp: BeautifulSoup, ref_map: Dict) -> Dict:
    """
    Generate table dict and replace with id tokens
    :param sp:
    :param ref_map:
    :return:
    """
    pass


def combine_ref_maps(eq_map: Dict, fig_map: Dict, tab_map: Dict, foot_map: Dict, sec_map: Dict):
    """
    Combine all items with ref ids into one map
    :param eq_map:
    :param fig_map:
    :param tab_map:
    :param sec_map:
    :return:
    """
    pass


def collapse_formatting_tags(sp: BeautifulSoup):
    """
    Collapse formatting tags like <hi>
    :param sp:
    :return:
    """
    pass


def process_abstract_from_tex(sp: BeautifulSoup, bib_map: Dict, ref_map: Dict) -> List[Dict]:
    """
    Parse abstract from soup
    :param sp:
    :param bib_map:
    :param ref_map:
    :return:
    """
    pass


def build_section_list(sec_id: str, ref_map: Dict) -> List[Tuple]:
    """
    Build list of sections from reference map from sec_id using parent entry recursively
    :param sec_id:
    :param ref_map:
    :return:
    """
    pass


def get_seclist_for_el(el: bs4.element.Tag, ref_map: Dict, default_seclist: List) -> List[Tuple]:
    """
    Build sec_list for tag
    :param el:
    :param ref_map:
    :param default_seclist:
    :return:
    """
    pass


def process_div(tag: bs4.element.Tag, secs: List, sp: BeautifulSoup, bib_map: Dict, ref_map: Dict) -> List[Dict]:
    """
    Process div recursively
    :param tag:
    :param secs:
    :param sp:
    :param bib_map:
    :param ref_map:
    :return:
    """
    pass


def process_body_text_from_tex(sp: BeautifulSoup, bib_map: Dict, ref_map: Dict) -> List[Dict]:
    """
    Parse body text from tag recursively
    :param sp:
    :param bib_map:
    :param ref_map:
    :return:
    """
    pass


def convert_xml_to_s2orc(
        sp: BeautifulSoup, file_id: str, year_str: str, log_file: str, grobid_config: Optional[Dict]=None
) -> Paper:
    """
    Convert a bunch of xml to gorc format
    :param sp:
    :param file_id:
    :param year_str:
    :param log_file:
    :param grobid_config:
    :return:
    """
    pass


def convert_latex_xml_to_s2orc_json(xml_fpath: str, log_dir: str, grobid_config: Optional[Dict]=None) -> Paper:
    """
    :param xml_fpath:
    :param log_dir:
    :param grobid_config:
    :return:
    """
    pass
