from json2html import json2html

test_json_records = [
    {
        "title": "Title #1",
        "body": "Hello, World 1!"
    },
    {
        "title": "Title #2",
        "body": "Hello, World 2!"
    }
]

required_html_string = "<h1>Title #1</h1><p>Hello, World 1!</p>"\
                        "<h1>Title #2</h1><p>Hello, World 2!</p>"


def test_json2html():
    result_html_string = json2html(test_json_records)
    assert result_html_string == required_html_string
