# from sections_check import missing_section, extra_section
# from evaluate_keywords import evaluate_keywords

def resume_score(cleaned_text, keywords=None, use_only_supplied_keywords=False, add_benchmark_sections=[], feedback=True):
    """
    This function uses the results of keyword and section analyses (from evaluate_keywords and sections_check) to give a 
    summary and a score that indicates of the quality of the resume text compared to the predefined baseline.

    Users can provide their own keywords or combine them with a default set of predefined keywords.
    Users can also provide names of additional sections to be checked.

    Parameters
    ----------
    cleaned_text : str
        The cleaned text content of the resume.
    keywords : list of str, optional
        A list of keywords to compare against the resume content. If not provided, only the baseline 
        keywords will be used. If `use_only_supplied_keywords` is set to True without supplying keywords, 
        no keywords will be used, and the function will return an empty result.
    use_only_supplied_keywords : bool, optional
        A flag to determine whether to use only the supplied keywords or to combine them with a default 
        set of predefined keywords. Defaults to False.
    add_benchmark_sections : list of str, optional
        A list of additional section names (e.g., ["Skills", "Education", "Work Experience", "Contact"]).
    feedback : bool, optional
        A flag to determine whether the summary should be included in the results (True), or just a line with
        the score should be given (False). The default is True.

    Returns
    -------
    str
        A string with a summary that gives the score of the given resume content. If feedback is True, lines
        explaining missing sections and keywords are also given.

    Examples
    --------
    >>> resume_text = '''
    ... Jane Doe
    ... Contact Information: janedoe@example.com
    ... Education: Master of Science in Data Science (2021)
    ... Work Experience: Data Scientist at Big Data Inc. (2022 - Present)
    ... Skills: Python, Machine Learning, SQL, Data Visualization
    ... '''
    >>> custom_keywords = ["Python", "Machine Learning", "SQL", "Big Data", "Cloud Computing"]
    >>> custom_sections = ["Certifications", "Projects"]
    >>> print(resume_score(
    ...     cleaned_text=resume_text,
    ...     keywords=custom_keywords,
    ...     use_only_supplied_keywords=False,
    ...     add_benchmark_sections=custom_sections
    ... ))

    This resume attained a score of 81.3.
    Feedback:
    - Missing Keywords: 'Big Data', 'Cloud Computing'
    - Missing Sections: 'Certifications', 'Projects'
    """