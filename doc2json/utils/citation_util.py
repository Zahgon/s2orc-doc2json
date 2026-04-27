# utility functions for handling failure situations with grobid-detected citation spans

import re
from typing import Dict, List, Tuple


BRACKET_REGEX = re.compile(r'\[[1-9]\d{0,2}([,;\-\s]+[1-9]\d{0,2})*;?\]')
BRACKET_STYLE_THRESHOLD = 5

SINGLE_BRACKET_REGEX = re.compile(r'\[([1-9]\d{0,2})\]')
EXPANSION_CHARS = {'-', 'â€“'}


def span_already_added(sub_start: int, sub_end: int, span_indices: List[Tuple[int, int]]) -> bool:
    """
    Check if span is a subspan of existing span
    :param sub_start:
    :param sub_end:
    :param span_indices:
    :return:
    """
    pass


def is_expansion_string(between_string: str) -> bool:
    """
    Check if the string between two refs is an expansion string
    :param between_string:
    :return:
    """
    pass


# TODO: still cases like `09bcee03baceb509d4fcf736fa1322cb8adf507f` w/ dups like ['L Jung', 'R Hessler', 'Louis Jung', 'Roland Hessler']
# example paper that has empties & duplicates: `09bce26cc7e825e15a4469e3e78b7a54898bb97f`
def _clean_empty_and_duplicate_authors_from_grobid_parse(authors: List[Dict]) -> List[Dict]:
    """
    Within affiliation, `location` is a dict with fields <settlement>, <region>, <country>, <postCode>, etc.
    Too much hassle, so just take the first one that's not empty.
    """
    pass
