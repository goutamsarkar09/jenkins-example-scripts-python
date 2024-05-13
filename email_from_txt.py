"""
This script extracts something between two tags in a text file using Python.
"""

import os
import sys

def fetch_required_input_files(input_file):
    try:
        # Check if input path exists
        if not os.path.exists(input_file):
            print("Input Filename:", input_file.split("/")[-1], "does not exist in the mentioned path")

    except Exception as e:
        print(e)
        sys.exit(1)

def extract_mail_data(input_file):
    with open(input_file, 'r') as input_csv:
        reader = input_csv.read()
        start = "<BODY_START>"
        end = "<BODY_END>"
        body_txt=reader[reader.index(start) + len(start): reader.index(end)]
        print(body_txt)
        return body_txt

def main1():
    if len(sys.argv) < 1:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    fetch_required_input_files(input_file)
    body_txt = extract_mail_data(input_file)
    return body_txt

if __name__ == '__main__':
    main1()
   
