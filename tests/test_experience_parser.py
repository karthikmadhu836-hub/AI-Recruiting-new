from ats_engine.experience_parser import *

def test_experience_parser():
    text = """
    ABC Tech (2021–2024)
    Software Developer
    XYZ Solutions (2020–2021)
    Intern
    """

    exp = extract_experience_blocks(text)
    roles = extract_roles(text)

    assert len(exp) > 0
    assert "developer" in roles