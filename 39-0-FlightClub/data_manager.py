import os
import requests

SHEETY_URL = os.environ["SHEETY_URL"]
SHEETY_AUTH = os.environ["SHEETY_AUTH"]


class DataManager:

    def __init__(self):
        self.cities = {}
        #This class is responsible for talking to the Google Sheet.

    def get_destinations(self):
        sheety_endpoint = SHEETY_URL
        sheety_headers = {
            "Authorization": f"Basic {SHEETY_AUTH}"
        }
        cities_response = requests.get(sheety_endpoint, headers=sheety_headers)
        cities_response.raise_for_status()
        self.cities = cities_response.json()
        self.cities = self.cities['prices']
        print(self.cities)

    def update_city_codes(self, iata_code, id):
        sheety_endpoint = f"{SHEETY_URL}/{id}"
        sheety_headers = {
            "Authorization": f"Basic {SHEETY_AUTH}"
        }
        sheety_data = {
            "price": {
                "iataCode": iata_code
            }
        }
        update_response = requests.put(sheety_endpoint, headers=sheety_headers, json=sheety_data)
        # self.update_response.raise_for_status()
        print(update_response)