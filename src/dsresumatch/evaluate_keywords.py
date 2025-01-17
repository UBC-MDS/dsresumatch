import json
from pathlib import Path

# load in baseline keywords
def load_baseline_keywords():
    """Load baseline keywords from the JSON file"""
    data_path = Path(__file__).parent / "data" / "baseline_keywords.json"
    with open(data_path, "r") as f:
        keywords_dict = json.load(f)
    
    # flatten all categories into a single list
    return [keyword.lower() for category in keywords_dict.values() for keyword in category]

def evaluate_keywords(cleaned_text, keywords=None, use_only_supplied_keywords=False):
    """
    Evaluate the quality of a resume by comparing its content against a set of predefined 
    or user-supplied keywords.

    This function assesses whether the resume contains relevant keywords that match the criteria 
    for a "good data science resume." Users can provide their own keywords or combine them with a 
    default set of predefined keywords.

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

    Returns
    -------
    list of str
        A list of keywords (from either the baseline or provided keywords) that do not appear 
        in the `cleaned_text`.

    Examples
    --------
    >>> evaluate_keywords("software development project management agile methodologies", ["software", "agile", "teamwork"])
    ['teamwork']

    >>> evaluate_keywords("data analysis machine learning statistical modeling", use_only_supplied_keywords=False)
    ['teamwork', 'communication']
    """
    
