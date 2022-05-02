from db import get_job_data
from job_roles import Services


services = Services()

def job_roles():
    """
    This function is used to predict the job roles of a user based on the
    job title.
    """
    job_data = get_job_data()
    job_title = job_data[0][0]
    job_roles = services.job_roles_prediction(job_title)
    return job_roles

def job_category():
    """
    This function is used to predict the job roles of a user based on the
    job description.
    """
    job_data = get_job_data()
    for job in job_data:
        job_title = job[0]
        print(job_title)
        print("--------")

        job_roles = services.job_category(job_title)
        print(job_roles)
        print("******************")


job_category()
