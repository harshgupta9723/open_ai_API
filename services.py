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
      
    def job_category(self, desc):
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
    
    def interview_question(self, job_role):
        """
        This function is used to generate the interview question based on
        job title.
        """
        
        url = os.getenv("URL")

        payload = json.dumps({
          "prompt": f"Create a list of 8 questions for my interview with a {job_role}:\n",
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

    def predict_benefits(self, desc):
        """
        This function is used to generate the interview question based on
        job title.
        """
        
        url = os.getenv("URL")

        payload = json.dumps({
          "prompt": f"Predict the job benefits :- {desc}:\n",
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

