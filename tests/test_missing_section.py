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
        ("", None, {"Skills", "Education", "Work Experience", "Contact"}),
        ("Skills: Python, Machine Learning\nEducation: B.Sc. in CS", [], {"Work Experience", "Contact"}),
        ("skills: Python\nEDUCATION: B.Sc. in CS", None, {"Work Experience", "Contact"}),
        ("Skills: Python\nEducation: CS\nContact: john.doe@example.com", None, {"Work Experience"}),
        ("Skills: Python, Machine Learning\nEducation: B.Sc. in CS", "Projects", {"Contact", "Work Experience", "Projects"}),
    ],
)
def test_missing_section_valid_cases(clean_text, add_benchmark_sections, expected_output):
    assert set(missing_section(clean_text, add_benchmark_sections)) == expected_output


# Parametrize for invalid inputs
@pytest.mark.parametrize(
    "clean_text, add_benchmark_sections, expected_exception",
    [
        (None, ["Skills", "Education"], TypeError),
        ("Skills: Python\nEducation: CS", 123, TypeError),
    ],
)
def test_missing_section_invalid_cases(clean_text, add_benchmark_sections, expected_exception):
    with pytest.raises(expected_exception):
        missing_section(clean_text, add_benchmark_sections)

