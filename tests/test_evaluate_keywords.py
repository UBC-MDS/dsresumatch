import pytest
from dsresumatch.evaluate_keywords import evaluate_keywords, load_baseline_keywords

# load baseline keywords once for all tests
BASELINE_KEYWORDS = load_baseline_keywords()

def test_baseline_keywords_loaded():
    """Test that baseline keywords are properly loaded"""
    
    keywords = load_baseline_keywords()
    assert "python" in keywords
    assert "teamwork" in keywords
    assert "docker" in keywords
    assert all(isinstance(keyword, str) for keyword in keywords)
    assert all(keyword.islower() for keyword in keywords) 

def test_only_supplied_keywords():
    """Test using only supplied keywords when use_only_supplied_keywords is True"""

    text = "python data analysis machine learning"
    keywords = ["python", "sql", "java"]
    result = evaluate_keywords(text, keywords, use_only_supplied_keywords=True)
    assert set(result) == {"sql", "java"}

def test_only_baseline_keywords():
    """Test using only baseline keywords when no keywords provided and use_only_supplied_keywords is False"""

    text = "python data analysis machine learning"
    result = evaluate_keywords(text, use_only_supplied_keywords=False)

    # We can now check specific baseline keywords
    assert "teamwork" in result  # from soft_skills
    assert "docker" in result    # from tools
    assert "pytorch" in result   # from technical_skills

def test_combined_keywords():
    """Test combining supplied and baseline keywords when use_only_supplied_keywords is False"""

    text = "python data analysis machine learning"
    keywords = ["python", "sql", "java"]
    result = evaluate_keywords(text, keywords, use_only_supplied_keywords=False)

    # Custom keywords that should be missing
    assert "sql" in result
    assert "java" in result

    # Baseline keywords that should be missing
    assert "teamwork" in result
    assert "docker" in result

def test_no_keywords_with_only_supplied():
    """Test when no keywords provided but use_only_supplied_keywords is True"""

    text = "python data analysis machine learning"
    
    # Check that warning is raised
    with pytest.warns(UserWarning, match="No keywords provided while use_only_supplied_keywords=True"):
        result = evaluate_keywords(text, use_only_supplied_keywords=True)
    
    assert result == []

def test_empty_text():
    """Test with empty text file"""

    text = ""
    
    # Check that warning is raised
    with pytest.warns(UserWarning, match="The provided resume text is an empty string"):
        result = evaluate_keywords(text)
    
    # All baseline keywords should be returned as missing
    assert set(result) == set(BASELINE_KEYWORDS)

def test_no_matches():
    """Test when no keywords match the text"""

    text = "completely irrelevant text"
    keywords = ["python", "sql", "java"]
    result = evaluate_keywords(text, keywords, use_only_supplied_keywords=True)
    assert set(result) == set(keywords)

def test_duplicate_baseline_keyword():
    """Test when supplied keyword already exists in baseline"""

    text = "python machine learning"

    # 'python' is in baseline keywords
    keywords = ["python", "sql"]
    result = evaluate_keywords(text, keywords, use_only_supplied_keywords=False)

    # 'python' should appear only once in results if missing
    assert len([k for k in result if k == "python"]) <= 1

def test_invalid_input_type():
    """Test with invalid input type"""

    text = "python data analysis"
    with pytest.raises((TypeError, ValueError)):
        evaluate_keywords(text, keywords=[1, 2, 3])

# used ChatGPT to include special/Non-English text
def test_special_characters():
    """Test with special characters and non-English text in keywords"""

    text = "python データサイエンス analysis"
    keywords = ["python", "データサイエンス", "R#", "C++"]
    result = evaluate_keywords(text, keywords, use_only_supplied_keywords=True)
    assert "python" not in result
    assert "データサイエンス" not in result
    assert "R#".lower() in result
    assert "C++".lower() in result

def test_case_sensitivity():
    """Test case sensitivity"""

    text = "PYTHON data ANALYSIS machine learning"
    keywords = ["python", "analysis", "SQL"]
    result = evaluate_keywords(text, keywords, use_only_supplied_keywords=True)

    # only SQL should be in results as python and analysis are in text (case-insensitive)
    assert result == ["sql"]

def test_empty_keywords_with_only_supplied():
    """Test when empty keywords list provided with use_only_supplied_keywords=True"""

    text = "python data analysis machine learning"
    
    # Check that warning is raised
    with pytest.warns(UserWarning, match="No keywords provided while use_only_supplied_keywords=True"):
        result = evaluate_keywords(text, keywords=[], use_only_supplied_keywords=True)
    
    assert result == []
