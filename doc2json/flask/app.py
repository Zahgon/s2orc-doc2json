"""
Flask app for S2ORC pdf2json utility
"""
import hashlib
import requests
from flask import Flask, request, jsonify, flash, url_for, redirect, render_template, send_file
from doc2json.grobid2json.process_pdf import process_pdf_stream
from doc2json.tex2json.process_tex import process_tex_stream
from doc2json.jats2json.process_jats import process_jats_stream

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'pdf', 'gz', 'nxml'}


@app.route('/')
def home():
    pass

@app.route('/', methods=['POST'])
def upload_file():
    pass

@app.route('/upload_url')
def upload_url():
    pass

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
