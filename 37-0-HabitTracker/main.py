import requests
import os
from datetime import datetime

USERNAME = os.environ.get("PIXELA_USERNAME")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Math Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# create a graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
yesterday = datetime(year=2024, month=8, day=2)

post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "45",
}

# response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
# print(response.text)


# update yesterday's pixel to 60 minutes instead
# with requests.put()

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

update_params = {
    "quantity": "60",
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

# delete yesterday's pixel
# with requests.delete()

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
