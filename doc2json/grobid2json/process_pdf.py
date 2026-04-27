import os
import json
import argparse
import time
from bs4 import BeautifulSoup
from typing import Optional, Dict

from doc2json.grobid2json.grobid.grobid_client import GrobidClient
from doc2json.grobid2json.tei_to_json import convert_tei_xml_file_to_s2orc_json, convert_tei_xml_soup_to_s2orc_json

BASE_TEMP_DIR = 'temp'
BASE_OUTPUT_DIR = 'output'
BASE_LOG_DIR = 'log'


def process_pdf_stream(input_file: str, sha: str, input_stream: bytes, grobid_config: Optional[Dict] = None) -> Dict:
    """
    Process PDF stream
    :param input_file:
    :param sha:
    :param input_stream:
    :return:
    """
    pass


def process_pdf_file(
        input_file: str,
        temp_dir: str = BASE_TEMP_DIR,
        output_dir: str = BASE_OUTPUT_DIR,
        grobid_config: Optional[Dict] = None
) -> str:
    """
    Process a PDF file and get JSON representation
    :param input_file:
    :param temp_dir:
    :param output_dir:
    :return:
    """
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run S2ORC PDF2JSON")
    parser.add_argument("-i", "--input", default=None, help="path to the input PDF file")
    parser.add_argument("-t", "--temp", default=BASE_TEMP_DIR, help="path to the temp dir for putting tei xml files")
    parser.add_argument("-o", "--output", default=BASE_OUTPUT_DIR, help="path to the output dir for putting json files")
    parser.add_argument("-k", "--keep", action='store_true')

    args = parser.parse_args()

    input_path = args.input
    temp_path = args.temp
    output_path = args.output
    keep_temp = args.keep

    start_time = time.time()

    os.makedirs(temp_path, exist_ok=True)
    os.makedirs(output_path, exist_ok=True)

    process_pdf_file(input_path, temp_path, output_path)

    runtime = round(time.time() - start_time, 3)
    print("runtime: %s seconds " % (runtime))
    print('done.')