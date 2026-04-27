"""

Functions for parsing specific `front_tag` soup tags

"""

from typing import Dict, List, Optional

from collections import Counter

import re


from doc2json.jats2json.pmc_utils.all_tag_utils import recurse_parse_section, parse_all_paragraphs_in_section, \
    replace_sup_sub_tags_with_string_placeholders, replace_xref_with_string_placeholders


class NoAuthorNamesError(Exception):
    """Known papers that trigger:
        - PMC3462967
    """
    pass


def parse_journal_id_tag(front_tag) -> str:
    """
    front_tag.find_all('journal-id') returns:
        [
            <journal-id journal-id-type="nlm-ta">Neurosci J</journal-id>,
            <journal-id journal-id-type="iso-abbrev">Neurosci J</journal-id>,
            <journal-id journal-id-type="publisher-id">NEUROSCIENCE</journal-id>
        ]
        [
            <journal-id journal-id-type="nlm-ta">BMC Biochem</journal-id>
            <journal-id journal-id-type="iso-abbrev">BMC Biochem</journal-id>
        ]
    """
    pass


def parse_journal_name_tag(front_tag) -> str:
    """
    Examples:
        # Paper 1
        <journal-title-group>
            <journal-title>BMC Biochemistry</journal-title>
        </journal-title-group>
        # Paper 2
        <journal-title-group>
            <journal-title>Neuroscience Journal</journal-title>
        </journal-title-group>

    But not all titles are contained within a `journal-title-group`.  See PMC1079901
        <journal-meta>
            <journal-id journal-id-type="nlm-ta">
                Biomed Eng Online
            </journal-id>
            <journal-title>
                BioMedical Engineering OnLine
            </journal-title>
        ...
    """
    pass


def parse_pubmed_id_tag(front_tag) -> Optional[str]:
    """Not every PMC paper has a PMID """
    pass


def parse_pmc_id_tag(front_tag) -> str:
    pass


def parse_doi_tag(front_tag) -> Optional[str]:
    """Not all papers have a DOI"""
    pass


def parse_title_tag(front_tag) -> str:
    """
    Examples:
        # Paper 1
        <title-group>
            <article-title>Role of the highly conserved G68 residue in the yeast phosphorelay protein Ypd1: implications for interactions between histidine phosphotransfer (HPt) and response regulator proteins</article-title>
        </title-group>
        # Paper 2
        <title-group>
            <article-title>Association of Strength and Physical Functions in People with Parkinson's Disease</article-title>
        </title-group>

    Want to restrict to `title-group` because sometimes title shows up in <notes> under self-citation
    """
    pass


def parse_category_tag(front_tag) -> List[str]:
    """
    Examples:
        # Paper 1
        <article-categories>
            <subj-group subj-group-type="heading">
                <subject>Research Article</subject>
            </subj-group>
        </article-categories>
        # Paper 2
        <article-categories>
            <subj-group subj-group-type="heading">
                <subject>Research Article</subject>
            </subj-group>
        </article-categories>
    """
    pass


def parse_date_tag(front_tag) -> Dict:
    """
    Two sets of tags contain dates:
        <pub-date pub-type="collection">
            <year>2018</year>
        </pub-date>
        <pub-date pub-type="epub">
            <day>12</day>
            <month>12</month>
            <year>2018</year>
        </pub-date>
    And:
        <history>
            <date date-type="received">
                <day>15</day>
                <month>10</month>
                <year>2018</year>
            </date>
            <date date-type="rev-recd">
                <day>20</day>
                <month>11</month>
                <year>2018</year>
            </date>
            <date date-type="accepted">
                <day>26</day>
                <month>11</month>
                <year>2018</year>
            </date>
        </history>

    PMC2557072 has `date` tag with no `day`, only `year` and `month`
    """
    pass


def parse_funding_groups(front_tag) -> List[str]:
    pass


# TODO: didnt want to handle <collab> group names; seemed rare and inconsistent; focus on <contrib> with <name> and <aff>
def parse_authors(front_tag) -> List[Dict]:
    pass


def parse_affiliations(front_tag) -> List[Dict]:
    """
    Sometimes affiliations is nested within '<contrib-group>' along with
    authors.  Sometimes, they're not and listed outside as multiple tags.

    Not all <aff> have IDs.  For example:
        <aff>St. Paul, Minnesota</aff>
    """
    pass


def parse_abstract_tag(front_tag, soup) -> List[Dict]:
    """Not every paper has an abstract

    Furthermore, note very abstract is structured into sections.
    Some abstracts (see PMC1914226) look like:
        <abstract>
            <p> ... </p>
            <p> ... </p>
        </abstract>
    """
    pass
