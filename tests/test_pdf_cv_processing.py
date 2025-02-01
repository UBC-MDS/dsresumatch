from collections import Counter
from dsresumatch.pdf_cv_processing import read_pdf, clean_text, count_words_in_pdf

def test_read_pdf():
    """Test cases for read_pdf function"""
    
    # Normal case
    result = read_pdf("tests/dummy.pdf")
    assert result == "Work Experience: Software Developer at XYZ Corp! "
    
    # Non-string input cases
    try:
        read_pdf(123)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")
    
    try:
        read_pdf(None)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")
    
    # Non-existent file case
    try:
        read_pdf("non_existent.pdf")
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("Expected FileNotFoundError")
    
    # Empty PDF case
    result = read_pdf("tests/empty.pdf")
    assert result == " "
    
    # Incorrect file type case
    try:
        read_pdf("tests/dummy.txt")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")

def test_clean_text():
    """Test cases for clean_text function"""

    try:
        clean_text(123)  # type: ignore
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")

    raw_text = "Work Experience: Software Developer at XYZ Corp!"
    expected_result = "work experience software developer xyz corp"
    result = clean_text(raw_text)
    assert result == expected_result


def test_count_words_in_pdf():
    """Test cases for count_words_in_pdf function"""
    
    try:
        count_words_in_pdf(123)  # type: ignore
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")
    # Simulate the output of read_pdf and clean_text
    pdf_text = "Work Experience: Software Developer at XYZ Corp!"
    expected_counter = Counter({
        "work": 1,
        "experience": 1,
        "software": 1,
        "developer": 1,
        "xyz": 1,
        "corp": 1
    })

    result = count_words_in_pdf("tests/dummy.pdf")
    assert result == expected_counter

def test_clean_text_with_empty_string():
    """Test case for clean_text with an empty string"""
    
    try:
        clean_text(None)  # type: ignore
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")
    
    raw_text = ""
    expected_result = ""
    result = clean_text(raw_text)
    assert result == expected_result


def test_count_words_in_pdf_with_empty_content():
    """Test case for count_words_in_pdf with an empty PDF"""
    try:
        count_words_in_pdf(None)  # type: ignore
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError")
    
    pdf_text = ""
    result = count_words_in_pdf("tests/empty.pdf")
    assert result == Counter()  # Empty Counter for empty content


def test_clean_text_removes_punctuation():
    """Test case for clean_text ensuring punctuation is removed"""

    raw_text = "Hello, world! Python programming is fun."
    expected_result = "hello world python programming fun"
    result = clean_text(raw_text)
    assert result == expected_result


def test_clean_text_removes_stopwords():
    """Test case for clean_text ensuring stopwords are removed"""

    raw_text = "This is a test for removing stopwords from text"
    expected_result = "test removing stopwords text"
    result = clean_text(raw_text)
    assert result == expected_result
