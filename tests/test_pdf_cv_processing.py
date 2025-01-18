from collections import Counter
from dsresumatch.pdf_cv_processing import read_pdf, clean_text, count_words_in_pdf

def test_read_pdf(): 
    result = read_pdf("tests/dummy.pdf")
    assert result == "Work Experience: Software Developer at XYZ Corp! "

def test_clean_text():
    raw_text = "Work Experience: Software Developer at XYZ Corp!"
    expected_result = "work experience software developer xyz corp"
    result = clean_text(raw_text)
    assert result == expected_result


def test_count_words_in_pdf():
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
    raw_text = ""
    expected_result = ""
    result = clean_text(raw_text)
    assert result == expected_result


def test_count_words_in_pdf_with_empty_content():
    pdf_text = ""
    result = count_words_in_pdf("tests/empty.pdf")
    assert result == Counter()  # Empty Counter for empty content


def test_clean_text_removes_punctuation():
    raw_text = "Hello, world! Python programming is fun."
    expected_result = "hello world python programming fun"
    result = clean_text(raw_text)
    assert result == expected_result


def test_clean_text_removes_stopwords():
    raw_text = "This is a test for removing stopwords from text"
    expected_result = "test removing stopwords text"
    result = clean_text(raw_text)
    assert result == expected_result
