import requests
from datetime import datetime

NUTRI_APP_ID = "925cd0bf"
NUTRI_API_KEY = "a904e7b895a1af1fbfbda3c9d9427392"
SHEETY_ENDPOINT = "https://api.sheety.co/6b6765598b14bcc76dd5f56907784aa4/workoutTracker/sheet1"

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_header = {"Authorization": "Bearer princeij"}

param = {
    "query": input("Tell me which exercise you did ? ")
}

header = {
    'x-app-id': NUTRI_APP_ID,
    'x-app-key': NUTRI_API_KEY

}

today = datetime.now()
response = requests.post(ENDPOINT, json=param, headers=header)
data = response.json()['exercises']

calories = [item['nf_calories'] for item in data]
exercise = [item['user_input'].title() for item in data]
duration = [item['duration_min'] for item in data]


for i in range(len(data)):
    rows = {
    "sheet1": {
    "date": today.strftime("%d/%m/%Y"),
    "time": today.strftime("%H:%M:%S"),
    "exercise": exercise[i],
    "duration": duration[i],
    "calories": calories[i]
        }
    }


    sheety = requests.post(SHEETY_ENDPOINT, json=rows, headers=sheet_header)
    print(f"Error: {sheety.status_code}, {sheety.text}")
