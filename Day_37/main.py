import requests
from datetime import datetime
TOKEN = "babucinaka"
USER = "princeij"
ENDPOINT= "https://pixe.la/v1/users"
GRAPH_ID = "firstgraph"
today = datetime.now()
DATE = today.strftime("%Y%m%d")
# Create Account

acct_param = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

graph_param = {
    "id": GRAPH_ID,
    "name": "Python Challenge",
    "unit": "days",
    "type": "int",
    "color": "sora"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(f"{ENDPOINT}", json=acct_param)
# print(response.text)

# graph = requests.put(f"{ENDPOINT}/{USER}/graphs/{GRAPH_ID}", json=graph_param, headers=header)
# print(graph.text)

posts = {
    "date": DATE,
    "quantity": input("How many days did you complete ? ")
}

post = requests.post(f"{ENDPOINT}/{USER}/graphs/{GRAPH_ID}", json=posts, headers=header)
print(post.text)

