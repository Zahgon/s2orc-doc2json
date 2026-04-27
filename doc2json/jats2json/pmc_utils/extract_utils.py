
from typing import Dict

import bs4
from bs4 import BeautifulSoup

from doc2json.jats2json.pmc_utils.all_tag_utils import parse_all_paragraphs_in_section


def extract_fig_blobs(body_tag) -> Dict:
    pass


def _update_fig_blobs(fig_blobs: Dict):
    pass


def extract_table_blobs(body_tag) -> Dict:
    # note 1: footnotes dont always exist for each table; hence the if statement
    # note 2: we want to preserve the XML tags for tables, but also need to run it through the regex cleaner for xrefs and other spans
    #         hence, wrapping all of the table XML text into a fake <p> paragraph tag
    pass


def _update_table_blobs(table_blobs: Dict):
    pass


def extract_suppl_blobs(body_tag) -> Dict:
    pass


def _update_suppl_blobs(suppl_blobs: Dict):
    pass
