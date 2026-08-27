import requests
import os

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = os.environ.get("PIXELA_GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
