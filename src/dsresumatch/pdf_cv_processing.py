def read_pdf(file_path):
    """
    Load text from a PDF file and return as a string.

    Parameters
    ----------
    file_path : str
        Path to the PDF file.

    Returns
    -------
    str
        PDF file contents as text.

    Examples
    --------
    >>> read_pdf("cv.pdf")
    'Work Experience\nSoftware Developer at XYZ Corp.\nEducation\nBachelor of Science in Computer Science\n'
    """

def identify_missing_sections(raw_text):
    """
    Identify missing predefined sections in the extracted text.

    Parameters
    ----------
    raw_text : str
        Text extracted from a PDF.

    Returns
    -------
    list
        A list of section headers that are missing in the text.

    Examples
    --------
    >>> raw_text = "Work Experience\nSoftware Developer at XYZ Corp.\n"
    >>> identify_missing_sections(raw_text)
    ['Education', 'Skills', 'Projects', 'Certifications', 'Awards']
    """


def count_words_in_pdf(file_path):
    """
    Count words in a PDF file.

    Words are made lowercase and punctuation, stop words in English are removed before counting.

    Parameters
    ----------
    file_path : str
        Path to the PDF file.

    Returns
    -------
    collections.Counter
        dict-like object where keys are words and values are counts.

    Examples
    --------
    >>> count_words_in_pdf("cv.pdf")
    Counter({'work': 1, 'experience': 1, 'software': 1, 'developer': 1, 'at': 1, 'xyz': 1, 'corp': 1, 'education': 1, 'bachelor': 1, 'of': 1, 'science': 1, 'in': 1, 'computer': 1})
    """

def clean_text(raw_text):
    """
    Lowercase and remove punctuation, and stop words from a string.

    Parameters
    ----------
    raw_text : str
        Text to clean.

    Returns
    -------
    str
        Cleaned text.

    Examples
    --------
    >>> clean_text("Work Experience: Software Developer at XYZ Corp!")
    'work experience software developer at xyz corp'
    """
