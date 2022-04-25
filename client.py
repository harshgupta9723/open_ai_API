from db import get_job_data
from job_roles import job_roles_prediction

def job_roles():
    """
    This function is used to predict the job roles of a user based on the
    job title.
    """
    job_data = get_job_data()
    job_description = job_data[0][0]
    job_roles = job_roles_prediction(job_description)
    return job_roles

job_roles = job_roles()
print(job_roles)