import re
import pytest
from dsresumatch.sections_check import missing_section 

# Parametrize for valid test cases
@pytest.mark.parametrize(
    "clean_text, add_benchmark_sections, expected_output",
    [
        ("Skills: Python, Machine Learning\nEducation: B.Sc. in CS", ["Work Experience", "Contact"], {"Work Experience", "Contact"}),
        ("""
        Skills: Python, Machine Learning
        Education: B.Sc. in CS
        Work Experience: Data Analyst
        Contact: john.doe@example.com
        """, None, set()),
        ("Skills: Python Education: CS\nContact: john.doe@example.com", ["Projects"], {"Work Experience", "Projects"}),
        ("Skills: Python, Machine Learning\nEducation: B.Sc. in CS", [], {"Work Experience", "Contact"}),
        ("skills: Python\nEDUCATION: B.Sc. in CS", None, {"Work Experience", "Contact"}),
        ("Skills: Python\nEducation: CS\nContact: john.doe@example.com", None, {"Work Experience"}),
        ("Skills: Python, Machine Learning\nEducation: B.Sc. in CS", "Projects", {"Contact", "Work Experience", "Projects"}),
    ],
)
def test_missing_section_valid_cases(clean_text, add_benchmark_sections, expected_output):
    """Tests valid inputs with various combinations of resume text and benchmark sections."""
    assert set(missing_section(clean_text, add_benchmark_sections)) == expected_output


# Parametrize for invalid inputs
@pytest.mark.parametrize(
    "clean_text, add_benchmark_sections, expected_exception",
    [
        (None, ["Skills", "Education"], TypeError),
        ("Skills: Python\nEducation: CS", 123, TypeError),
        ("Skills: Python\nEducation: CS", True, TypeError),
        ("Skills: Python\nEducation: CS", False, TypeError)
    ],
)
def test_missing_section_invalid_cases(clean_text, add_benchmark_sections, expected_exception):
    """Tests invalid inputs where TypeError is expected."""
    with pytest.raises(expected_exception):
        missing_section(clean_text, add_benchmark_sections)

def test_missing_section_warning_empty_text():
    """Tests warning behavior when an empty string is passed as the resume text."""
    clean_text = ""
    expected_output = ["Skills", "Education", "Work Experience", "Contact"]
    with pytest.warns(UserWarning, match="The provided resume text is an empty string. Returning all benchmark sections as missing."):
        assert set(missing_section(clean_text)) == set(expected_output)
