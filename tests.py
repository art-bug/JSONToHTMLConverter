from json2html import json2html

test_json_records = [
    {
        "h3": "Title #1",
        "div": "Hello, World 1!"
    }
]

required_html_string = "<h3>Title #1</h3><div>Hello, World 1!</div>"


def test_json2html():
    result_html_string = json2html(test_json_records)
    assert result_html_string == required_html_string
