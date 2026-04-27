from typing import Dict, List, Callable

import re
import itertools

from bs4 import BeautifulSoup

START_TOKENS = {"#!start#", "@!start@", "&!start&"}
SEP_TOKENS = {"#!sep#"}
END_TOKENS = {"#!end#", "@!end@", "&!end&"}
ALL_TOKENS = START_TOKENS | SEP_TOKENS | END_TOKENS


def replace_xref_with_string_placeholders(soup_tag, soup):
    # replace all xref tags with string placeholders
    pass


def replace_sup_sub_tags_with_string_placeholders(soup_tag, soup):
    # replace all sup/sub tags with string placeholders
    pass


def recurse_parse_section(
    sec_tag,
    # suppl_blobs: Dict
) -> List[Dict]:
    """Recursive function for getting paragraph blobs to look like
        {
            'text': ...,
            ...,
            'section': SUBSUBSECTION_NAME :: SUBSECTION_NAME :: SECTION_NAME
        }
    """
    pass


def _reduce_args(stack: List, end_token: str) -> List[List]:
    """Helper function for `_parse_all_paragraphs_in_section`.
    
    Pop arguments for the xref off the top of the stack and return a list of argument lists,
    where the outer lists represent groups divided by separators."""
    pass


def _add_spans(
    end_token: str,
    start_pos: int,
    text: str,
    ref_id,
    ref_type,
    cite_spans: List,
    fig_spans: List,
    table_spans: List,
    sup_spans: List,
    sub_spans: List,
):
    """Helper function used by `_parse_all_paragraphs_in_section`."""
    pass


def get_latex_from_formula(
    formula_tag
):
    pass


def get_mathml_from_formula(
    formula_tag
):
    pass


def parse_formulas(
    para_el,
    sp,
    replace
):
    # sub and get corresponding spans of inline formulas
    pass


def parse_all_paragraphs_in_section(
    sec_tag,
    par_to_text: Callable = None,
    replace_formula=True
) -> List[Dict]:
    """Internal function. Assumes section has no nested tags
    `par_to_text` is an optional function that converts the `par` tag into a string.  by default, calls `par_tag.text`.
    """
    pass
