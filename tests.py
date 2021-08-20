from json2html import record2html, json2html

test_json_records = [
    {
        "h3": "Title #1",
        "div": "Hello, World 1!"
    },
    {
        "h3": "Title #2",
        "div": "Hello, World 2!"
    }
]


def test_record2html():
    required_first_record_html = "<h3>Title #1</h3><div>Hello, World 1!</div>"

    result_record_html = record2html(test_json_records[0])
    assert result_record_html == required_first_record_html


def test_wrapped_json2html():
    required_list = ['<h3>Title #1</h3><div>Hello, World 1!</div>',
                     '<h3>Title #2</h3><div>Hello, World 2!</div>']

    orig_json2html = json2html.__wrapped__

    result_list = orig_json2html(test_json_records)
    assert result_list == required_list


def test_json2html():
    required_html = "<ul><li><h3>Title #1</h3><div>Hello, World 1!</div>"\
                    "</li><li><h3>Title #2</h3><div>Hello, World 2!</div>"\
                    "</li></ul>"

    result_html_string = json2html(test_json_records)
    assert result_html_string == required_html
