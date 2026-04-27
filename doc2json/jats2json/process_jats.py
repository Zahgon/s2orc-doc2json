import os
import json
import argparse
import time
from typing import Optional

from doc2json.jats2json.jats_to_json import convert_jats_xml_to_s2orc_json


BASE_TEMP_DIR = 'temp'
BASE_OUTPUT_DIR = 'output'
BASE_LOG_DIR = 'log'


def process_jats_stream(
        fname: str,
        stream: bytes,
        temp_dir: str=BASE_TEMP_DIR
):
    """
    Process a jats file stream
    :param fname:
    :param stream:
    :param temp_dir:
    :return:
    """
    pass


def process_jats_file(
        jats_file: str,
        output_dir: str=BASE_OUTPUT_DIR,
        log_dir: str=BASE_LOG_DIR,
) -> Optional[str]:
    """
    Process files in a JATS XML file and get JSON representation
    :param jats_file:
    :param output_dir:
    :param log_dir:
    :return:
    """
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run S2ORC JATS2JSON")
    parser.add_argument("-i", "--input", default=None, help="path to the input JATS XML file")
    parser.add_argument("-o", "--output", default='output', help="path to the output dir for putting json files")
    parser.add_argument("-l", "--log", default='log', help="path to the log dir")

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    log_path = args.log

    start_time = time.time()

    os.makedirs(output_path, exist_ok=True)

    process_jats_file(input_path, output_path, log_path)

    runtime = round(time.time() - start_time, 3)
    print("runtime: %s seconds " % (runtime))
    print('done.')
