"""
Process all the files in a LaTeX zip file to extract paper content

1. Unzips LaTeX ZIP file
2. Identifies primary TEX file
3. Expands other TEX files into main TEX file using latexpand
4. Expands BBL file into main TEX file
5. Convert TEX file into XML using tralics
6. Extract content of XML into S2ORC JSON

"""

import os
import gzip
import tarfile
import zipfile
import shutil
from typing import Optional

from doc2json.utils.latex_util import normalize, latex_to_xml


def _is_gzip_file(fpath):
    pass


def extract_latex(zip_file: str, latex_dir: str, cleanup=True):
    """
    Unzip latex zip into temp directory
    :param zip_file:
    :param latex_dir:
    :param cleanup:
    :return:
    """
    pass


def normalize_latex(latex_dir: str, norm_dir: str, norm_log_file: str, cleanup=True) -> Optional[str]:
    """
    Normalize all latex files from arxiv
    :param latex_dir:
    :param norm_dir:
    :param norm_log_file:
    :param cleanup:
    :return:
    """
    pass


def norm_latex_to_xml(norm_dir: str, xml_dir: str, xml_err_file: str, xml_log_file: str, cleanup=True) -> Optional[str]:
    """
    Convert LaTeX to XML using tralics
    :param norm_dir:
    :param xml_dir:
    :param xml_err_file:
    :param xml_log_file:
    :param cleanup:
    :return:
    """
    pass


def convert_latex_to_xml(
        zip_file: str, latex_dir: str, norm_dir: str, xml_dir: str, log_dir: str, cleanup=True
) -> Optional[str]:
    """
    Run expansion, normalization, xml conversion on latex
    :param zip_file:
    :param latex_dir:
    :param norm_dir:
    :param xml_dir:
    :param log_dir:
    :param cleanup:
    :return:
    """
    pass


def convert_latex_to_s2orc_json(
        latex_zip: str,
        base_temp_dir: str,
        cleanup_after: bool=True
) -> str:
    """
    Convert a LaTeX zip file to S2ORC JSON
    :param latex_zip:
    :param base_temp_dir:
    :param cleanup_after:
    :return:
    """
    pass
