import requests
import os
from datetime import datetime

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = os.environ.get("PIXELA_GRAPH_ID")

pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "1"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(
    url=pixel_endpoint,
    json=pixel_data,
    headers=headers
)

print(response.text)
