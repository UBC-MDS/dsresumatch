import pytest
import os
import sys

# Access parent folder and import necessary packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from dsresumatch.resume_scoring import resume_score

# Setting up Test Data
clean_text_optimal = """
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

clean_text_blank = ""
keywords_optimal = ["TensorFlow", "Altair", "ggplot", "R", "Python"]
keywords_blank = []
benchmark_sections_optimal = ["volunteer Work", "References"]
benchmark_sections_blank = []

clean_text_wrong_type = 55
keywords_wrong_type = True
benchmark_sections_wrong_type = "Test"
use_only_supplied_keywords_wrong_type = 11.1
feedback_wrong_type = []


# Create testing functions

def resume_score_test_cleaned_text_only():
    """Testing cleaned_text is a string, no optional variables."""
    expected_result = """
    This resume attained a score of 81.3.
    Feedback:
    - Missing Keywords: 'Big Data', 'Cloud Computing'
    - Missing Sections: 'Certifications', 'Projects'
    """
    actual_result = resume_score(clean_text_optimal)
    assert actual_result == expected_result, "resume_score_test_cleaned_text_only failed."

def resume_score_test_cleaned_text_feedback():
    """Testing cleaned_text is a string, with feedback = False"""
    expected_result = """
    This resume attained a score of 81.3.
    """
    actual_result = resume_score(clean_text_optimal, 
                                 feedback=False)
    assert actual_result == expected_result, "resume_score_test_cleaned_text_feedback failed."

def resume_score_test_cleaned_text_keywords():
    """Testing cleaned_text is a string, with keywords provided."""
    expected_result = """
    This resume attained a score of 85.3.
    Feedback:
    - Missing Keywords: 'Big Data', 'Cloud Computing'
    - Missing Sections: 'Certifications', 'Projects'
    """
    actual_result = resume_score(clean_text_optimal, 
                                 keywords=keywords_optimal)
    assert actual_result == expected_result, "resume_score_test_cleaned_text_keywords failed."

def resume_score_test_cleaned_text_keywords_only():
    """Testing cleaned_text is a string, with keywords provided and use_only_supplied_keywords = True"""
    expected_result = """
    This resume attained a score of 95.
    Feedback:
    - Missing Keywords: 'Big Data'
    """
    actual_result = resume_score(clean_text_optimal, 
                                 keywords=keywords_optimal, 
                                 use_only_supplied_keywords=True)
    assert actual_result == expected_result, "resume_score_test_cleaned_text_keywords_only failed."

def resume_score_test_cleaned_text_benchmark_sections():
    """Testing cleaned_text is a string, with benchmark_sections provided."""
    expected_result = """
    This resume attained a score of 95.
    Feedback:
    - Missing Keywords: 'Big Data'
    """
    actual_result = resume_score(clean_text_optimal, 
                                 add_benchmark_sections=benchmark_sections_optimal)
    assert actual_result == expected_result, "resume_score_test_cleaned_text_benchmark_sections failed."

def resume_score_test_cleaned_text_all_arguments():
    """Testing cleaned_text is a string, with all arguments."""
    expected_result = """
    This resume attained a score of 81.3.
    """
    actual_result = resume_score(clean_text_optimal, 
                                 feedback=False, 
                                 keywords=keywords_optimal, 
                                 use_only_supplied_keywords=True,
                                 add_benchmark_sections=benchmark_sections_optimal)
    assert actual_result == expected_result, "resume_score_test_cleaned_text_all_arguments failed."
