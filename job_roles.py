import requests
import json
import os

def job_roles_prediction(job_title):
    """
    This function is used to predict the job roles of a user based on the
    job title.
    """
    
    url = os.getenv("URL")

    payload = json.dumps({
      "prompt": "Job roles for "+ job_title +" jobs in USA",
      "temperature": 0,
      "max_tokens": 60,
      "top_p": 1,
      "frequency_penalty": 0,
      "presence_penalty": 0
    })
    headers = {
      'Authorization': os.getenv('KEY'),
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()['choices'][0]['text']

