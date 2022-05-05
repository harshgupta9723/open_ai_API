#connect mysql to python
import os
import sqlalchemy
from sqlalchemy import create_engine


def get_connection():

    user = os.getenv("DBUSER")
    pwd = os.getenv("DBPASS")
    host = os.getenv("DBHOST")
    database = os.getenv("DBNAME")
    dbport = os.getenv("DBPORT")

    con_string = "mysql+pymysql://{}:{}@{}:{}/{}".format(
        user, pwd, host, dbport, database)

    # create engine
    sqlEngine = create_engine(con_string, pool_recycle=3600)
    db = sqlEngine.raw_connection()

    return db


def get_job_data():
    """
    This function is used to get the job roles from the database.
    """
    db = get_connection()
    
    cursor = db.cursor()
    query = "SELECT distinct(job_title), clean_job_description FROM job where html_job_description != '' limit 10"
    cursor.execute(query)
    results = cursor.fetchall()
    return results
