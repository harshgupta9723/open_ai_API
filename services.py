#name this file services

import requests
import json
import os

class Services:

    def __init__(self):
        print("Running services")

    def job_roles_prediction(self, job_title):
        """
        This function is used to predict the job roles of a user based on the
        job title.
        """
        
        url = os.getenv("URL")

        payload = json.dumps({
          "prompt": f"{job_title} job title\n\nlist of distinct job roles:",
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
      
    def job_category_prediction(self, desc):
        """
        This function is used to generate the interview question based on
        job title.
        """
        
        url = os.getenv("URL")

        payload = json.dumps({
          "prompt": f"{desc}\n\nCategory:",
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


    def job_benefits_prediction(self, desc):

        url = os.getenv("URL")

        payload = json.dumps({
          "prompt": f"{desc}\n\nQ. what are benefits of this job?",
          "temperature": 0,
          "max_tokens": 100,
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


    def job_qualification_prediction(self, desc):

        url = os.getenv("URL")

        payload = json.dumps({
          "prompt": f"{desc}\n\nQ. What qualifications are needed for this job?",
          "temperature": 0,
          "max_tokens": 100,
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
