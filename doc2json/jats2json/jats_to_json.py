"""
Mostly copied from cite2vec paper_parsing.parse_nxml
"""

from typing import List, Set, Dict, Callable

import os
import json
import re
import multiprocessing
from bs4 import BeautifulSoup
from tqdm import tqdm
from glob import glob
from pprint import pprint

from doc2json.utils.soup_utils import destroy_unimportant_tags_inplace
from doc2json.jats2json.pmc_utils.front_tag_utils import parse_journal_id_tag, parse_journal_name_tag, \
    parse_title_tag, parse_category_tag, parse_date_tag, parse_doi_tag, parse_pmc_id_tag, parse_pubmed_id_tag, \
    parse_authors, parse_affiliations, parse_abstract_tag, parse_funding_groups, NoAuthorNamesError
from doc2json.jats2json.pmc_utils.extract_utils import extract_fig_blobs, extract_table_blobs, extract_suppl_blobs
from doc2json.jats2json.pmc_utils.all_tag_utils import replace_xref_with_string_placeholders, \
    replace_sup_sub_tags_with_string_placeholders, recurse_parse_section
from doc2json.jats2json.pmc_utils.all_tag_utils import parse_all_paragraphs_in_section
from doc2json.jats2json.pmc_utils.back_tag_utils import parse_bib_entries

from doc2json.s2orc import Paper


def process_front_tag(front_tag, soup) -> Dict:
    # process <journal-meta> tags
    pass


def process_body_tag(body_tag, soup) -> Dict:
    # replace all xref tags with string placeholders
    pass


def process_back_tag(back_tag) -> Dict:
    # glossary = {}
    # if back_tag.find('glossary'):
    #     for def_item_tag in back_tag.find('glossary').find_all('def-item'):
    #         glossary[def_item_tag.find('term').text] = def_item_tag.find('def').text

    # TODO: author contrib and COIs
    # notes = []
    # for notes_tag in back_tag.find_all('notes'):
    #     pass

    # TODO: PMC2778891 has back tag that looks like:  <back><sec><title>Acknowledgements</title><p>Supported by the Austrian Science Fund (P-20670 and W11).</p></sec></back>
    #       that is, it doesn't have 'ack' section.
    pass


def postprocess_front_tags_for_s2orc(init_front_dict: Dict):
    """
    Fix authors and year for S2ORC format
    """
    pass


def convert_acks_to_s2orc(paragraphs: List) -> List[Dict]:
    """
    Convert acks to S2ORC paragraphs
    """
    pass


def convert_paragraphs_to_s2orc(paragraphs: List, old_to_new: Dict) -> List[Dict]:
    """
    Convert paragraphs into S2ORC format
    """
    pass


def convert_jats_xml_to_s2orc_json(jats_file: str, log_dir: str):
    """
    Convert JATS XML to S2ORC JSON
    :param jats_file:
    :param log_dir:
    :return:
    """
    pass


if __name__ == '__main__':
    jats_file = 'tests/jats/PMC5828200.nxml'
    paper = convert_jats_xml_to_s2orc_json(jats_file, 'logs')

    jats_file = 'tests/jats/PMC6398430.nxml'
    paper = convert_jats_xml_to_s2orc_json(jats_file, 'logs')

    jats_file = 'tests/jats/PMC7417471.nxml'
    paper = convert_jats_xml_to_s2orc_json(jats_file, 'logs')

    print('done.')