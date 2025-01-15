import re

def missing_section(clean_text, add_benchmark_sections=None):
    """
    Identifies the sections missing from the resume based on the benchmark sections.

    Parameters:
    ----------
    clean_text : str
        The text extracted from the resume.
    add_benchmark_sections : list of str, optional
        A list of additional section names (e.g., "Skills", "Education", 
        "Work Experience", "Contact"). Defaults to None.

    Returns:
    -------
    list of str
        A list of section names from the benchmark that are not present in the resume.
    
    Examples:
    --------
    # Example 1: With custom benchmark sections
    clean_text = "Skills: Python, Machine Learning\nEducation: B.Sc. in CS"
    add_benchmark_sections = ["Skills", "Education", "Work Experience", "Contact"]
    missing = missing_section(clean_text, add_benchmark_sections)
    # Output: ['Work Experience', 'Contact']

    # Example 2: Without benchmark sections (None)
    clean_text = "Skills: Python, Machine Learning\nEducation: B.Sc. in CS"
    missing = missing_section(clean_text)
    # Output: [] or custom logic for None case
    """
    if add_benchmark_sections is not None and not (isinstance(add_benchmark_sections, list) or isinstance(add_benchmark_sections, str)):
        raise TypeError("Expected a string, list, or None for additional benchmark sections.")

    # Define hardcoded benchmark sections as a set
    benchmark_sections = {"Skills", "Education", "Work Experience", "Contact"}

    # Convert the single string to a list if necessary
    if isinstance(add_benchmark_sections, str):
        add_benchmark_sections = [add_benchmark_sections]

    # Add additional benchmark sections if provided
    if add_benchmark_sections:
        benchmark_sections.update(add_benchmark_sections)

    # Identify sections missing from the resume using regex
    missing = []
    for section in benchmark_sections:
        # Regex pattern to match section names (case-insensitive, handles concatenation)
        pattern = rf"\b{re.escape(section)}\b"
        if not re.search(pattern, clean_text, re.IGNORECASE):
            missing.append(section)

    return missing

def extra_section(resume_text, add_benchmark_sections=None):
    """
    Identifies the sections present in the resume that are not part of the benchmark sections.

    Parameters:
    ----------
    resume_text : str
        The text extracted from the resume.
    add_benchmark_sections : list of str, optional
        A list of additional section names (e.g., "Skills", "Education", 
        "Work Experience", "Contact"). Defaults to None.

    Returns:
    -------
    list of str
        A list of section names that are present in the resume but not part of the benchmark.
    
    # Example 1: With custom benchmark sections
    resume_text = "Skills: Python, Machine Learning\nProjects: Deep Learning"
    add_benchmark_sections = ["Skills", "Education", "Work Experience", "Contact"]
    extra = extra_section(resume_text, add_benchmark_sections)
    # Output: ['Projects']

    # Example 2: Without benchmark sections (None)
    resume_text = "Skills: Python, Machine Learning\nProjects: Deep Learning"
    extra = extra_section(resume_text)
    # Output: ['Projects'] or custom logic for None case
    """
