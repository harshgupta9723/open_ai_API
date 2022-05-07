from db import get_job_data
from services import Services
import re


services = Services()


def cleaner(test_string):
    """
    This function is used to clean the job title string.
    """
    test_string = test_string.replace("\n", ", ")
    test_string = test_string.replace("-", " ")
    #remove numerical values from string
    test_string = re.sub(r'\d+', '', test_string)
    #remove . from string
    test_string = test_string.replace(".", "")
    test_string = test_string.replace("  ", "")

    final_string = list(set(test_string.split(",")))
    
    # check if "" is in the list
    if ' ' in final_string:
        final_string.remove(' ')
    
    if '' in final_string:
        final_string.remove('')
    
    return final_string


def job_type_parser(desc_list):
    types = []
    for i in desc_list:
        desc = i
        text = desc.replace("/n","")
        if "full time" in text:
            types.append("Full Time")
        elif "part time" in text:
            types.append("Part Time")
        elif "both" in text:
            types.append("Part Time and Full Time")
    return types


def extract_salary(s):
    """
    This function is used to extract salary form a given
    job description
    """
    
    if "$" in s:
        return s[s.index('$'):]
    else:
        return s    


def job_roles(job_title):
    """
    This function is used to predict the job roles of a user based on the
    job title.
    """
    
    job_role = services.job_roles_prediction(job_title)

    clean_job_roles = cleaner(job_role)
    
    return clean_job_roles
    

def job_category(job_description):
    """
    This function is used to generate job category based on
    job description.
    """

    job_category = services.job_category_prediction(job_description)

    try:
        job_category = job_category.split('of ', 1)[1]
    except:
        pass

    job_category = cleaner(job_category)

    return job_category


def job_benefits(job_description):
    """
    This function is used to generate job benefits based on
    job description.
    """

    job_benefits = services.job_benefits_prediction(job_description)
    
    #'A.' means answer.
    try:
        job_benefits = job_benefits.split('A. ', 1)[1]
    except:
        pass
    
    return job_benefits
        

def job_qualifications(job_description):
    """
    This function is used to generate job qualifications based on
    job description.
    """

    job_qualifications = services.job_qualification_prediction(job_description)
    
    try:
        job_qualifications = job_qualifications.split('A. ', 1)[1]
    except:
        pass

    return job_qualifications


def job_requriments(job_description):
    """
    This function is used to generate the job requriments based on
    job description.
    """
    
    job_requirenment = services.job_requriment_prediction(job_description)

    job_requirenment = cleaner(job_requirenment)

    return job_requirenment
       

def job_salary_prediction(job_description):
    """
    This function is used to extract salary form a given 
    job description
    """
    
    job_salary = services.job_salary_prediction(job_description)
    job_salary = extract_salary(job_salary)
    
    return job_salary


def job_type_prediction(job_description):
    """
    This function is used to extract type of a job form a given 
    job description
    """

    job_type = services.job_type_prediction(job_description)
    job_type = cleaner(job_type)
    job_type = job_type_parser(job_type)

    return job_type


if __name__ == "__main__":
    
    job_data = get_job_data()
    
    for job in job_data:
        job_title = job[0]
        job_description = job[1]
        
        job_roles(job_title)
        job_category(job_description)
        job_benefits(job_description)
        job_qualifications(job_description)
        job_requriments(job_description)
        job_salary_prediction(job_description)
        job_type_prediction(job_description)