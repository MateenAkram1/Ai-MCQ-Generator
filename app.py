from flask import Flask, request, render_template, send_file
import os
import pdfplumber
import docx
import csv
from werkzeug.utils import secure_filename
import google.generativeai as genai
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Handle the form submission and generate the MCQs
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)