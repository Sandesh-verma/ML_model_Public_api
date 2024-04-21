# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 22:54:32 2024

@author: sande
"""

import json 
import requests

url =' https://8735-2409-408c-8dc5-6467-3cd1-9deb-9d65-d11a.ngrok-free.app/diabetes_prediction'

input_data_for_model = {
    
    'Pregnancies' : 6,
    'Glucose' : 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)