import os
import io
import json
import argparse
import time
import glob
from doc2json.grobid2json.grobid.client import ApiClient
import ntpath
from typing import List

'''
This version uses the standard ProcessPoolExecutor for parallelizing the concurrent calls to the GROBID services.
Given the limits of ThreadPoolExecutor (input stored in memory, blocking Executor.map until the whole input
is acquired), it works with batches of PDF of a size indicated in the config.json file (default is 1000 entries).
We are moving from first batch to the second one only when the first is entirely processed - which means it is
slightly sub-optimal, but should scale better. However acquiring a list of million of files in directories would
require something scalable too, which is not implemented for the moment.
'''

DEFAULT_GROBID_CONFIG = {
    "grobid_server": "localhost",
    "grobid_port": "8070",
    "batch_size": 1000,
    "sleep_time": 5,
    "generateIDs": False,
    "consolidate_header": False,
    "consolidate_citations": False,
    "include_raw_citations": True,
    "include_raw_affiliations": False,
    "max_workers": 2,
}

class GrobidClient(ApiClient):

    def __init__(self, config=None):
        self.config = config or DEFAULT_GROBID_CONFIG
        self.generate_ids = self.config["generateIDs"]
        self.consolidate_header = self.config["consolidate_header"]
        self.consolidate_citations = self.config["consolidate_citations"]
        self.include_raw_citations = self.config["include_raw_citations"]
        self.include_raw_affiliations = self.config["include_raw_affiliations"]
        self.max_workers = self.config["max_workers"]
        self.grobid_server = self.config["grobid_server"]
        self.grobid_port = self.config["grobid_port"]
        self.sleep_time = self.config["sleep_time"]

    def process(self, input: str, output: str, service: str):
        pass

    def process_batch(self, pdf_files: List[str], output: str, service: str) -> None:
        pass

    def process_pdf_stream(self, pdf_file: str, pdf_strm: bytes, output: str, service: str) -> str:
        # process the stream
        pass

    def process_pdf(self, pdf_file: str, output: str, service: str) -> None:
        # check if TEI file is already produced
        # we use ntpath here to be sure it will work on Windows too
        pass

    def process_citation(self, bib_string: str, log_file: str) -> str:
        # process citation raw string and return corresponding dict
        pass

    def process_header_names(self, header_string: str, log_file: str) -> str:
        # process author names from header string
        pass

    def process_affiliations(self, aff_string: str, log_file: str) -> str:
        # process affiliation from input string
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Client for GROBID services")
    parser.add_argument("service", help="one of [processFulltextDocument, processHeaderDocument, processReferences]")
    parser.add_argument("--input", default=None, help="path to the directory containing PDF to process")
    parser.add_argument("--output", default=None, help="path to the directory where to put the results")
    parser.add_argument("--config", default=None, help="path to the config file, default is ./config.json")

    args = parser.parse_args()

    input_path = args.input
    config = json.load(open(args.config)) if args.config else DEFAULT_GROBID_CONFIG
    output_path = args.output
    service = args.service

    client = GrobidClient(config=config)

    start_time = time.time()

    client.process(input_path, output_path, service)

    runtime = round(time.time() - start_time, 3)
    print("runtime: %s seconds " % (runtime))
