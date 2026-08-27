import requests
import os
from datetime import datetime
x_app_id = os.environ.get("X_APP_ID")
x_app_key = os.environ.get("X_APP_KEY")
x_app_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"


sheety_url = "https://api.sheety.co/850b3246b1898b9a7e2c6a80e48ec6ff/myWorkout/sheet1"
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

query = input("Tell me which exercise you did: ")
headers = {
    "Content-Type": "application/json",
    "x-app-id" : x_app_id,
    "x-app-key" : x_app_key
}

parameters = {
    "query": query
}

response = requests.post(url=x_app_endpoint,
                        json=parameters,
                        headers=headers)
response.raise_for_status()

result = response.json()
# print(result["exercises"][0])
exercise = result["exercises"][0]["name"].title()
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

sheety_headers = {
    "Authorization": os.environ.get("Authorization")
}

body = {
    "sheet1": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}


response = requests.post(url=sheety_url,
                         json=body,
                         headers=sheety_headers)
data = response.json()
print(data)

print(response.status_code)
print(response.text)
