def read_pdf(file_path):
    """
    Extract text content from a PDF file and return it as a single consolidated string.

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


def count_words_in_pdf(file_path):
    """
    Count the frequency of words in a PDF file.

    This function converts all words to lowercase, removing punctuation, and excluding common English stop words to ensure meaningful word counts. 

    Parameters
    ----------
    file_path : str
        Path to the PDF file.

    Returns
    -------
    collections.Counter
        dictionary-like object with the frequency of each remaining words where keys are words and values are counts.

    Examples
    --------
    >>> count_words_in_pdf("cv.pdf")
    Counter({'work': 1, 'experience': 1, 'software': 1, 'developer': 1, 'at': 1, 'xyz': 1, 'corp': 1, 'education': 1, 'bachelor': 1, 'of': 1, 'science': 1, 'in': 1, 'computer': 1})
    """

def clean_text(raw_text):
    """
    Covert raw_text to lowercase, remove punctuation, and filter out common English stop words to retain only meaningful words in the string.

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
    'work experience software developer xyz corp'
    """
