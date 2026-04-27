from typing import List, Tuple


def replace_refspans(
    spans_to_replace: List[Tuple[int, int, str, str]],
    full_string: str,
    pre_padding: str = "",
    post_padding: str = "",
    btwn_padding: str = ", "
) -> str:
    """
    For each span within the full string, replace that span with new text
    :param spans_to_replace: list of tuples of form (start_ind, end_ind, span_text, new_substring)
    :param full_string:
    :param pre_padding:
    :param post_padding:
    :param btwn_padding:
    :return:
    """
    pass


def sub_spans_and_update_indices(
    spans_to_replace: List[Tuple[int, int, str, str]],
    full_string: str
) -> Tuple[str, List]:
    """
    Replace all spans and recompute indices
    :param spans_to_replace:
    :param full_string:
    :return:
    """
    pass


