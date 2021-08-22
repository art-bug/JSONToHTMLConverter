from json2html import record2html, json2html

test_json_records = [
    {
        "span": "Title #1",
        "content": [
            {
                "p": "Example 1",
                "header": "header 1"
            }
        ]
    },
    {
        "div": "div 1"
    }
]


def test_record2html():
    required_first_record_html = "<span>Title #1</span><content>"\
                                 "<ul><li><p>Example 1</p>"\
                                 "<header>header 1</header></li></ul>"\
                                 "</content>"

    result_record_html = record2html(test_json_records[0])
    assert result_record_html == required_first_record_html


def test_json2html():
    required_html = "<ul><li><span>Title #1</span><content><ul><li>"\
                    "<p>Example 1</p><header>header 1</header></li></ul>"\
                    "</content></li><li><div>div 1</div></li></ul>"

    result_html_string = json2html(test_json_records)
    assert result_html_string == required_html
