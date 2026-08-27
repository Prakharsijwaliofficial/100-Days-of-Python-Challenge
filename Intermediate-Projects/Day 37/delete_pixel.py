import requests
import os
from datetime import datetime

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = os.environ.get("PIXELA_GRAPH_ID")

today = datetime.now().strftime("%Y%m%d")

delete_endpoint = (
    f"https://pixe.la/v1/users/{USERNAME}/graphs/"
    f"{GRAPH_ID}/{today}"
)

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.delete(
    url=delete_endpoint,
    headers=headers
)

print(response.text)
