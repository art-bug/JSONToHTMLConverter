'''
     This module contains the json2html function and various auxiliary
     functions and decorators for the task of
     conversion JSON file 'records'-like content to a HTML string.
'''

import argparse
import json
import os
from collections.abc import Iterable
from typing import List
import functools
import re
import html


def parse_css_selector(selector: str):
    '''
        Parses the CSS selector to the list of three items -
        tag, id and class list.
    '''

    _tag = re.match(r"[a-z]+[1-9]?", selector).group()
    _id = str()
    classes = []

    if '#' in selector:
        _id = re.search(r"(?<=#)([\w-]+)", selector).group()

    if '.' in selector:
        classes = re.findall(r"(?<=\.)([\w-]+)", selector)

    return [_tag, _id, classes]


def tag(html_tag: str, text: str):
    '''
        Frames text with the HTML tag, the text escapes.
    '''

    _tag, _id, classes = parse_css_selector(html_tag)
    _id = f" id=\"{_id}\"" if _id else ''
    _class = f" class=\"{' '.join(classes)}\"" if classes else ''

    escaped_text = html.escape(text)

    return f"<{_tag}{_id}{_class}>{escaped_text}</{_tag}>"


def record2html(json_record: dict):
    '''
        Converts JSON 'record' to a HTML string.
    '''

    return ''.join(tag(html_tag, text) if type(text) is not list
                   else tag(html_tag, json2html(text))
                   for html_tag, text in json_record.items())


def html_list(html_elements: Iterable[str]):
    '''
        Represents the HTML elements as a HTML list.
    '''

    return tag('ul', ''.join(tag('li', el) for el in html_elements))


def as_html_list(func):
    '''
        This decorator represents the HTML elements got from func
        as a HTML list string.
    '''

    def wrapper(*args, **kwargs):
        html_elements = func(*args, **kwargs)

        return html_list(html_elements)

    functools.update_wrapper(wrapper, func)

    wrapper.__doc__ = "Converts JSON file 'records'-like content to "\
                      "a HTML list string."

    return wrapper


def as_html_string(func):
    '''
        This decorator represents the HTML elements got from func
        as a HTML string.
    '''

    def wrapper(*args, **kwargs):
        html_elements = func(*args, **kwargs)

        return ''.join(html_elements)

    functools.update_wrapper(wrapper, func)

    wrapper.__doc__ = "Converts JSON file 'records'-like content to "\
                      "a HTML string."

    return wrapper


@as_html_string
def json2html(json_records: List[dict] or dict):
    '''
        Converts JSON file 'records'-like content to list of HTML elements.
    '''

    if isinstance(json_records, dict):
        return [record2html(json_records)]

    return [record2html(record) for record in json_records]


def __file_path(path: str):
    error_string = f"Given path {path} is not a valid path."

    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(error_string)

    return path


def __parse_arguments():
    description = "Convert JSON file in 'records' format to HTML file."
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
    arguments = __parse_arguments()

    json_obj = {}

    with open(arguments.input_json_file, 'r') as json_file:
        json_obj = json.load(json_file)

    result_html = json2html(json_obj)

    with open(arguments.output_html_file, 'w') as html_file:
        html_file.write(result_html)
