from parsers.education_parser import extract_education

def test_education_parser():
    text = "B.Tech Computer Science 2021"

    result = extract_education(text)

    assert len(result) > 0
    assert result[0]["degree"] == "B.Tech"