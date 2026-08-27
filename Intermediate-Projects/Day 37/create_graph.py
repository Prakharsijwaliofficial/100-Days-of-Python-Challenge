import requests
import os

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_config = {
    "id": "codinggraph",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(
    url=graph_endpoint,
    json=graph_config,
    headers=headers
)

print(response.text)
