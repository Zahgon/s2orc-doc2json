"""
Many of the REGEX expressions and pipeline in this set of utilities are borrowed or extended from
the unarXive project: https://github.com/IllDepence/unarXive

Modifications have been made to better identify the primary latex file and expand all other latex
files into the main file. Latexpand and tralics options have also been changed.
"""
import chardet
import magic
import os
import re
import glob
import subprocess
import tempfile

MAIN_TEX_PATT = re.compile(r'(\\begin\s*\{\s*document\s*\})', re.I)
# ^ with capturing parentheses so that the pattern can be used for splitting
PDF_EXT_PATT = re.compile(r'^\.pdf$', re.I)
GZ_EXT_PATT = re.compile(r'^\.gz$', re.I)
TEX_EXT_PATT = re.compile(r'^\.tex$', re.I)
NON_TEXT_PATT = re.compile(r'^\.(pdf|eps|jpg|png|gif)$', re.I)
BBL_SIGN = '\\bibitem'
# natbib fix
PRE_FIX_NATBIB = True
NATBIB_PATT = re.compile((r'\\cite(t|p|alt|alp|author|year|yearpar)\s*?\*?\s*?'
                           '(\[[^\]]*?\]\s*?)*?\s*?\*?\s*?\{([^\}]+?)\}'),
                         re.I)
# bibitem option fix
PRE_FIX_BIBOPT = True
BIBOPT_PATT = re.compile(r'\\bibitem\s*?\[[^]]*?\]', re.I|re.M)

# â†‘ above two solve most tralics problems; except for mnras style bibitems
# (https://ctan.org/pkg/mnras)

# agressive math pre-removal
PRE_FILTER_MATH = False
FILTER_PATTS = []
for env in ['equation', 'displaymath', 'array', 'eqnarray', 'align', 'gather',
            'multline', 'flalign', 'alignat']:
    s = r'\\begin\{{{0}[*]?\}}.+?\\end\{{{0}\}}'.format(env)
    patt = re.compile(s, re.I | re.M | re.S)
    FILTER_PATTS.append(patt)
FILTER_PATTS.append(re.compile(r'\$\$.+?\$\$', re.S))
FILTER_PATTS.append(re.compile(r'\$.+?\$', re.S))
FILTER_PATTS.append(re.compile(r'\\\(.+?\\\)', re.S))
FILTER_PATTS.append(re.compile(r'\\\[.+?\\\]', re.S))


def read_file(path):
    pass


def remove_math(latex_str):
    pass


def normalize(path, out_dir, write_logs=True):
    """
    Normalize an arXiv file
    Adapted from https://github.com/IllDepence/unarXive
        with modifications

    Identifies the primary *.tex file, the bibliography file,
    and expands other tex files and the bibliography into the
    main tex file
    """
    pass


def latex_to_xml(tex_file: str, out_dir: str, out_file: str, err_file: str, log_file: str):
    """
    Convert expanded latex file to XML using tralics
    :param tex_file:
    :param out_dir:
    :param out_file:
    :param err_file:
    :param log_file:
    :return:
    """
    pass
