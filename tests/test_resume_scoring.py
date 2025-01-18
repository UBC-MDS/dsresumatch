import pytest

# Access package and import necessary packages
from dsresumatch.resume_scoring import resume_score

# Setting up Test Data
@pytest.fixture
def test_data():

    test = {}

    test["clean_text_optimal"] = """
    John Doe  
    123 Main Street  
    City, State, ZIP  
    john.doe@example.com  
    (123) 456-7890  
    LinkedIn: linkedin.com/in/johndoe  

    Objective  
    Dedicated Data Scientist with 3 years of experience in statistical analysis, machine learning, and data visualization. Seeking a role where I can contribute to data-driven decision-making processes and solve complex business problems.  

    Education  
    Master of Science in Data Science  
    University of ABC, May 2021  
    - Relevant coursework: Machine Learning, Statistical Inference, Data Mining, Big Data Analytics  

    Bachelor of Science in Mathematics  
    University of XYZ, May 2019  
    - Relevant coursework: Linear Algebra, Probability, Calculus, Numerical Methods  

    Technical Skills  
    - Programming Languages: Python, R, SQL  
    - Data Visualization: Altair, Tableau, ggplot2  
    - Machine Learning: scikit-learn, TensorFlow, Keras  
    - Databases: MySQL, PostgreSQL  
    - Other: Git, Linux, Jupyter Notebooks  

    Professional Experience  
    Data Scientist  
    Company ABC, City, State  
    June 2021 – Present  
    - Designed and implemented machine learning models to predict customer churn, improving retention by 15%  
    - Automated data pipelines, reducing data processing time by 30%  
    - Developed interactive dashboards using Altair to visualize key performance indicators  
    - Conducted A/B testing for marketing campaigns, leading to a 10% increase in click-through rates  

    Data Analyst Intern  
    Company XYZ, City, State  
    May 2020 – August 2020  
    - Analyzed customer data to identify trends, improving client segmentation strategy  
    - Created reports using R and Tableau, presenting findings to stakeholders  
    - Collaborated with a team of 5 to clean and preprocess large datasets for analysis  

    Projects  
    - Linear Programming Optimization: Developed a Python tool using PuLP to optimize resource allocation for a manufacturing process  
    - Movie Recommendation System: Built a collaborative filtering model using scikit-learn to suggest movies based on user ratings  
    - Interactive COVID-19 Dashboard: Created an Altair-based visualization of pandemic trends across countries  

    Achievements  
    - Dean’s List (5 semesters)  
    - Presented research paper at Data Science Conference 2020  
    - Earned “Employee of the Month” recognition for outstanding project performance  

    Interests  
    - Open-source contributions  
    - Competitive programming  
    - Hiking and photography  
    """

    test["clean_text_blank"] = ""
    test["keywords_optimal"] = ["TensorFlow", "Altair", "ggplot", "R", "Python"]
    test["keywords_blank"] = []
    test["benchmark_sections_optimal"] = ["volunteer Work", "References"]
    test["benchmark_sections_blank"] = []

    test["clean_text_wrong_type"] = 55
    test["keywords_wrong_type"] = True
    test["benchmark_sections_wrong_type"] = "Test"
    test["use_only_supplied_keywords_wrong_type"] = 11.1
    test["feedback_wrong_type"] = []

    return test

# Create testing functions

def test_resume_score_cleaned_text_only(test_data):
    """Testing cleaned_text is a string, no optional variables."""
    expected_result = """
    This resume attained a score of 50.00.
    - Missing Keywords: aws, project management, teamwork, problem solving, numpy, communication, pandas, data analysis, statistics, docker, pytorch, leadership
    - Missing Sections: Contact, Work Experience
    """
    actual_result = resume_score(test_data["clean_text_optimal"])
    assert actual_result == expected_result, "resume_score_test_cleaned_text_only failed."

def test_resume_score_cleaned_text_feedback(test_data):
    """Testing cleaned_text is a string, with feedback = False"""
    expected_result = """
    This resume attained a score of 50.00.
    """
    actual_result = resume_score(test_data["clean_text_optimal"], 
                                 feedback=False)
    assert actual_result == expected_result, "resume_score_test_cleaned_text_feedback failed."

def test_resume_score_cleaned_text_keywords(test_data):
    """Testing cleaned_text is a string, with keywords provided."""
    expected_result = """
    his resume attained a score of 57.58.
    Feedback:
    - Missing Keywords: 'Big Data', 'Cloud Computing'
    - Missing Sections: 'Certifications', 'Projects'
    """
    actual_result = resume_score(test_data["clean_text_optimal"], 
                                 keywords=test_data["keywords_optimal"])
    assert actual_result == expected_result, "resume_score_test_cleaned_text_keywords failed."

def test_resume_score_cleaned_text_keywords_only(test_data):
    """Testing cleaned_text is a string, with keywords provided and use_only_supplied_keywords = True"""
    expected_result = """
    This resume attained a score of 84.62.
    Feedback:
    - Missing Keywords: 'Big Data'
    """
    actual_result = resume_score(test_data["clean_text_optimal"], 
                                 keywords=test_data["keywords_optimal"], 
                                 use_only_supplied_keywords=True)
    assert actual_result == expected_result, "resume_score_test_cleaned_text_keywords_only failed."

def test_resume_score_cleaned_text_benchmark_sections(test_data):
    """Testing cleaned_text is a string, with benchmark_sections provided."""
    expected_result = """
    This resume attained a score of .
    Feedback:
    - Missing Keywords: 'Big Data'
    """
    actual_result = resume_score(test_data["clean_text_optimal"], 
                                 add_benchmark_sections=test_data["benchmark_sections_optimal"])
    assert actual_result == expected_result, "resume_score_test_cleaned_text_benchmark_sections failed."

def test_resume_score_cleaned_text_all_arguments(test_data):
    """Testing cleaned_text is a string, with all arguments."""
    expected_result = """
    This resume attained a score of 81.3.
    """
    actual_result = resume_score(test_data["clean_text_optimal"], 
                                 feedback=False, 
                                 keywords=test_data["keywords_optimal"], 
                                 use_only_supplied_keywords=True,
                                 add_benchmark_sections=test_data["benchmark_sections_optimal"])
    assert actual_result == expected_result, "resume_score_test_cleaned_text_all_arguments failed."

def test_resume_score_clean_text_blank(test_data):
    """Testing cleaned_text is blank, feedback = False."""
    expected_result = """
    This resume attained a score of 0.
    """
    actual_result = resume_score(test_data["clean_text_blank"],
                                feedback = False)
    
    with pytest.warns(UserWarning):
        assert actual_result == expected_result, "test_resume_score_clean_text_blank failed."

def test_resume_score_keywords_blank(test_data):
    """Testing cleaned_text is given, keywords is blank, feedback = False."""
    expected_result = """
    This resume attained a score of _.
    """
    actual_result = resume_score(test_data["clean_text_optimal"],
                                 keywords = test_data["keywords_blank"],
                                 feedback = False)
    
    with pytest.warns(UserWarning):
        assert actual_result == expected_result, "test_resume_score_keywords_blank failed."

def test_resume_score_benchmark_blank(test_data):
    """Testing cleaned_text is given, add_benchmark_section is blank, feedback = False."""
    expected_result = """
    This resume attained a score of _.
    """
    actual_result = resume_score(test_data["clean_text_optimal"],
                                 add_benchmark_sections=test_data["benchmark_sections_blank"],
                                feedback = False)
    
    with pytest.warns(UserWarning):
        assert actual_result == expected_result, "test_resume_score_benchmark_blank failed."

def test_resume_score_keywords_only_blank(test_data):
    """Testing cleaned_text is given, keywords is blank, use_only_supplied_keywords=True, feedback = False."""
    expected_result = """
    This resume attained a score of _.
    """
    actual_result = resume_score(test_data["clean_text_optimal"],
                                 keywords = test_data["keywords_blank"],
                                 use_only_supplied_keywords=True,
                                 feedback = False)
    
    with pytest.warns(UserWarning):
        assert actual_result == expected_result, "test_resume_score_keywords_only_blank failed."

def test_resume_score_keywords_only_no_keywords(test_data):
    """Testing cleaned_text is given, keywords is not given, use_only_supplied_keywords=True, feedback = False."""
    expected_result = """
    This resume attained a score of _.
    """
    actual_result = resume_score(test_data["clean_text_optimal"],
                                 use_only_supplied_keywords=True,
                                 feedback = False)
    
    with pytest.warns(UserWarning):
        assert actual_result == expected_result, "test_resume_score_keywords_only_no_keywords failed."

def test_resume_score_cleaned_text_wrong_type(test_data):
    """Testing cleaned_text is wrong data type."""
    with pytest.raises(TypeError):
        resume_score(cleaned_text=test_data["clean_text_wrong_type"])

def test_resume_score_keywords_wrong_type(test_data):
    """Testing keywords is wrong data type."""
    with pytest.raises(TypeError):
        resume_score(cleaned_text=test_data["clean_text_optimal"],
                     keywords=test_data["keywords_wrong_type"])

def test_resume_score_keywords_only_wrong_type(test_data):
    """Testing use_only_supplied_keywords is wrong data type."""
    with pytest.raises(TypeError):
        resume_score(cleaned_text=test_data["clean_text_optimal"],
                     keywords=test_data["keywords_optimal"],
                     use_only_supplied_keywords=test_data["use_only_supplied_keywords_wrong_type"])
        
def test_resume_score_benchmark_sections_wrong_type(test_data):
    """Testing add_benchmark_sections is wrong data type."""
    with pytest.raises(TypeError):
        resume_score(cleaned_text=test_data["clean_text_optimal"],
                     add_benchmark_sections=test_data["benchmark_sections_wrong_type"])

def test_resume_score_feedback_wrong_type(test_data):
    """Testing feedback is wrong data type."""
    with pytest.raises(TypeError):
        resume_score(cleaned_text=test_data["clean_text_optimal"],
                     feedback=test_data["feedback_wrong_type"])