import os
import json
import argparse
import time
from typing import Dict

from doc2json.spp2json.spp.spp_client import SppClient
from doc2json.spp2json.spp.spp_json_to_s2orc_json import convert_spp_json_to_s2orc_json



def process_pdf_file(input_file: str, temp_dir: str, output_dir: str) -> str:
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
    parser.add_argument("-t", "--temp", default='temp/', help="path to the temp dir for putting tei xml files")
    parser.add_argument("-o", "--output", default='output/', help="path to the output dir for putting json files")
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