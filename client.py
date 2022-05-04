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


def job_roles():
    """
    This function is used to predict the job roles of a user based on the
    job title.
    """
    job_data = get_job_data()
    
    JOB_TITLE = 0
    
    for job in job_data:
        job_title = job[JOB_TITLE]
        job_role = services.job_roles_prediction(job_title)

        clean_job_roles = cleaner(job_role)
        
        print(clean_job_roles)
    
def job_category():
    """
    This function is used to generate the interview question based on
    job description.
    """
    job_data = get_job_data()
    
    JOB_DESCRIPTION = 1
    
    for job in job_data:
        job_description = job[JOB_DESCRIPTION]
        job_category = services.job_category_prediction(job_description)

        job_category = cleaner(job_category)

        print(job_category[0].replace(' Category:', ''))
       
       
job_category() 
job_roles()