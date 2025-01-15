 
from dsresumatch.sections_check import missing_section 
import re

# Test cases for the `missing_section` function
def test_missing_section():
    # --- Expected Use Cases ---
    # Case 1: Resume missing some sections
    clean_text_1 = "Skills: Python, Machine Learning\nEducation: B.Sc. in CS"
    add_benchmark_sections_1 = ["Work Experience", "Contact"]
    expected_output_1 = {"Work Experience", "Contact"}
    assert set(missing_section(clean_text_1, add_benchmark_sections_1)) == expected_output_1

    # Case 2: Resume has all sections (no missing sections)
    clean_text_2 = """
    Skills: Python, Machine Learning
    Education: B.Sc. in CS
    Work Experience: Data Analyst
    Contact: john.doe@example.com
    """
    add_benchmark_sections_2 = None  
    expected_output_2 = []
    assert missing_section(clean_text_2, add_benchmark_sections_2) == expected_output_2

    # Case 3: Additional benchmark sections provided
    clean_text_3 = "Skills: Python Education: CS\nContact: john.doe@example.com"
    add_benchmark_sections_3 = ["Projects"]
    expected_output_3 = {"Work Experience", "Projects"}
    assert set(missing_section(clean_text_3, add_benchmark_sections_3)) == expected_output_3

    # --- Edge Cases ---
    # Case 4: Empty resume text
    clean_text_4 = ""
    expected_output_4 = {"Skills", "Education", "Work Experience", "Contact"}
    assert set(missing_section(clean_text_4)) == expected_output_4

    # Case 5: Empty additional benchmark sections
    clean_text_5 = "Skills: Python, Machine Learning\nEducation: B.Sc. in CS"
    add_benchmark_sections_5 = []
    expected_output_5 = {"Work Experience", "Contact"}
    assert set(missing_section(clean_text_5, add_benchmark_sections_5)) == expected_output_5

    # Case 6: Case-insensitive matching
    clean_text_6 = "skills: Python\nEDUCATION: B.Sc. in CS"
    add_benchmark_sections_6 = None
    expected_output_6 = {"Work Experience", "Contact"}
    assert set(missing_section(clean_text_6, add_benchmark_sections_6)) == expected_output_6

    # Case 7: Clean text contain words that are sticked together
    clean_text_7 = "Skills: Python\nEducation: CS\nContact: john.doe@example.com"
    expected_output_7 = {"Work Experience"}
    assert set(missing_section(clean_text_7)) == expected_output_7

    # Case 8: Non-list additional benchmark sections (single string)
    clean_text_8 = "Skills: Python, Machine Learning\nEducation: B.Sc. in CS"
    add_benchmark_sections_8 = "Projects"  # A string, not a list
    expected_output_8 = {"Contact", "Work Experience", "Projects"}
    assert set(missing_section(clean_text_8, add_benchmark_sections_8)) == expected_output_8

    # --- Error Cases ---
    # Case 9: Non-string resume text
    clean_text_9 = None
    add_benchmark_sections_9 = ["Skills", "Education"]
    try:
        missing_section(clean_text_9, add_benchmark_sections_9)
        assert False, "Expected TypeError for non-string resume text"
    except TypeError:
        pass

    # Case 10: Invalid type for additional benchmark sections (non-string, non-list)
    clean_text_10 = "Skills: Python\nEducation: CS"
    add_benchmark_sections_10 = 123  # Invalid input (integer)
    try:
        missing_section(clean_text_10, add_benchmark_sections_10)
        assert False, "Expected TypeError for invalid additional benchmark section type"
    except TypeError:
        pass  # This is expected behavior
    
