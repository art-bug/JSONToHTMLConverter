from json2html import parse_css_selector, tag, json2html

test_json_dict = {
    "p.my-class#my-id": "hello",
    "p.my-class1.my-class2": "example<a>asd</a>"
}


def test_parse_css_selector_with_tag_only():
    required_result = ['p', '', []]

    parsed_selector = parse_css_selector('p')
    assert parsed_selector == required_result


def test_parse_css_selector_with_numeric_tag_and_titlecase_id():
    required_result = ['h1', "My-id", []]

    parsed_selector = parse_css_selector("h1#My-id")
    assert parsed_selector == required_result


def test_parse_css_selector_with_numeric_tag_and_titlecase_class():
    required_result = ['h1', '', ["My-Class"]]

    parsed_selector = parse_css_selector("h1.My-Class")
    assert parsed_selector == required_result


def test_parse_css_selector_with_elements_of_one_by_each_type():
    required_result = ['p', "my-id", ["my-class"]]

    selector = list(test_json_dict.keys())[0]
    parsed_selector = parse_css_selector(selector)

    assert parsed_selector == required_result


def test_parse_css_selector_with_multiple_classes():
    required_result = ['p', '', ["my-class1", "my-class2"]]

    selector = list(test_json_dict.keys())[1]
    parsed_selector = parse_css_selector(selector)

    assert parsed_selector == required_result


def test_tag_with_tag_only():
    required_result = "<p>text</p>"

    tagged_text = tag('p', "text")
    assert tagged_text == required_result


def test_tag_with_numeric_tag_and_titlecase_id():
    required_result = "<h1 id=\"My-id\">text</h1>"

    tagged_text = tag("h1#My-id", "text")
    assert tagged_text == required_result


def test_tag_with_numeric_tag_and_titlecase_class():
    required_result = "<h1 class=\"My-Class\">text</h1>"

    tagged_text = tag("h1.My-Class", "text")
    assert tagged_text == required_result


def test_tag_with_elements_of_one_by_each_type():
    required_result = "<p id=\"my-id\" class=\"my-class\">hello</p>"

    tagged_text = tag(*list(test_json_dict.items())[0])
    assert tagged_text == required_result


def test_tag_with_multiple_classes():
    required_result = "<p class=\"my-class1 my-class2\">text</p>"

    selector = list(test_json_dict.keys())[1]
    tagged_text = tag(selector, "text")
    assert tagged_text == required_result


def test_json2html():
    required_html = "<p id=\"my-id\" class=\"my-class\">hello</p>"\
                    "<p class=\"my-class1 my-class2\">"\
                    "example&lt;a&gt;asd&lt;/a&gt;</p>"

    result_html_string = json2html(test_json_dict)
    assert result_html_string == required_html
