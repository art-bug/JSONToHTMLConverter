'''
     This module contains single json2html function
     that converts JSON 'records'-like content to HTML string.
'''

import argparse
import os
import json


def tag(html_tag: str, text: str):
    '''
        Frames text with the HTML tag.
    '''

    return f"<{html_tag}>{text}</{html_tag}>"


def json2html(json_records: list):
    '''
        Converts JSON file 'records'-like content to HTML string.
    '''

    return ''.join(tag(html_tag, text) for record in json_records
                   for html_tag, text in record.items())


def __file_path(path: str):
    error_string = f"Given path {path} is not a valid path."

    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(error_string)

    return path


def __parse_arguments():
    description = "Convert JSON file content in 'records' format to HTML file."
    argparser = argparse.ArgumentParser(description=description)

    input_help = "Input JSON file in 'records' format."
    output_help = "Output HTML file."

    in_dest = "input_json_file"
    out_dest = "output_html_file"

    argparser.add_argument("-i", "--in", "--input", default="source.json",
                           type=__file_path, help=input_help, dest=in_dest)

    argparser.add_argument("-o", "--out", "--output", default="index.html",
                           type=__file_path, help=output_help, dest=out_dest)

    return argparser.parse_args()


if __name__ == "__main__":
    args = __parse_arguments()

    json_obj = {}

    with open(args.input_json_file, 'r') as json_file:
        json_obj = json.load(json_file)

    result_html = json2html(json_obj)

    with open(args.output_html_file, 'w') as html_file:
        html_file.write(result_html)
