import os
import requests

AMADEUS_ID = os.environ["AMADEUS_ID"]
AMADEUS_SECRET = os.environ["AMADEUS_SECRET"]
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

class FlightSearch:

    def __init__(self):
        #This class is responsible for talking to the Flight Search API.
        self.amadeus_token = str(self.get_token())
        self.amadeus_token_url = TOKEN_ENDPOINT
        self.amadeus_city_url = CITY_ENDPOINT
        self.city = ""
        self.city_code = ""


    def get_token(self):
        self.amadeus_token_url = TOKEN_ENDPOINT
        amadeus_token_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        amadeus_token_data = {
            "grant_type": "client_credentials",
            "client_id": AMADEUS_ID,
            "client_secret": AMADEUS_SECRET
        }
        amadeus_token_response = requests.post(
            self.amadeus_token_url,
            data=amadeus_token_data,
            headers=amadeus_token_headers
        )
        amadeus_token_response.raise_for_status()
        amadeus_token_data = amadeus_token_response.json()
        # print(amadeus_token_data)
        self.amadeus_token = amadeus_token_data['access_token']
        return self.amadeus_token

    def get_city_code(self, destination_city):
        self.city = destination_city
        amadeus_city_headers = {
            "Authorization": f"Bearer {self.amadeus_token}"
        }
        amadeus_city_params = {
            "keyword": self.city,
        }
        amadeus_city_response = requests.get(
            self.amadeus_city_url,
            params=amadeus_city_params,
            headers=amadeus_city_headers
            )
        amadeus_city_response.raise_for_status()
        if amadeus_city_response.status_code == 401:
            print("renewing token")
            self.get_token()
            self.get_city_code(self.city)
        amadeus_city_data = amadeus_city_response.json()
        # print(amadeus_city_data)
        self.city_code = amadeus_city_data['data'][0]['iataCode']
        return self.city_code
