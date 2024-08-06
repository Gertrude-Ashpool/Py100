import requests
import datetime as dt
import os

GENDER = "male"
WEIGHT_KG = "80"
HEIGHT_CM = "180"
AGE = "40"

# Nutritionix
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety
SHEETY_URL = os.environ["SHEETY_URL"]
SHEETY_AUTH = os.environ["SHEETY_AUTH"]


def get_exercise_data(query):
    nutritionix_url = ENDPOINT
    nutritionix_headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY
    }
    nutritionix_params = {
        "query": f"{query}",
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    nutritionix_response = requests.post(nutritionix_url, json=nutritionix_params, headers=nutritionix_headers)
    nutritionix_response.raise_for_status()
    nutritionix_data = nutritionix_response.json()
    nutritionix_exercises = nutritionix_data['exercises']
    return nutritionix_exercises


exercise_data = get_exercise_data(input("Tell me which exercises you did "))
print(exercise_data)

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

for exercise in exercise_data:
    now = dt.datetime.now()
    sheety_endpoint = SHEETY_URL
    sheety_headers = {
        "Authorization": f"Basic {SHEETY_AUTH}"
    }
    new_row = {
        "workout": {
            "date": str(today_date),
            "time": str(now_time),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    new_row_response = requests.post(sheety_endpoint, headers=sheety_headers, json=new_row)
    new_row_response.raise_for_status()
    print(new_row_response.text)
