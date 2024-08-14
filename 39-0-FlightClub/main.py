#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import datetime as dt
import os
from flight_search import FlightSearch
from data_manager import DataManager
import pprint as pprint

# Sheety
SHEETY_URL = os.environ["SHEETY_URL"]
SHEETY_AUTH = os.environ["SHEETY_AUTH"]

flight_search = FlightSearch()
data_manager = DataManager()

ORIGIN_IATA_CODE = "LON"

sheety_data = [
    {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
    {'city': 'Frankfurt', 'iataCode': 'FRA', 'lowestPrice': 42, 'id': 3},
    {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
    {'city': 'Hong Kong', 'iataCode': 'HKG', 'lowestPrice': 551, 'id': 5},
    {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
    {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
    {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
    {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
    {'city': 'Dublin', 'iataCode': 'DBN', 'lowestPrice': 378, 'id': 10}
]


# print("Data from Sheety:")
# print(data_manager.get_destinations())


# check if sheety data has the iata city codes.
# if not, look up from amadeus and update sheety entry
for city in sheety_data:
    if not city['iataCode']:
        city['iataCode'] = flight_search.get_city_code(city['city'])
        print(city['iataCode'])
        data_manager.update_city_codes(str(city['iataCode']), str(city['id']))


print(sheety_data)

# generate date strings
today_date = dt.datetime.now()
tomorrow_date = today_date + dt.timedelta(days=1)
tomorrow_date = tomorrow_date.strftime("%Y-%m-%d")
date_in_six_months = today_date + dt.timedelta(days=180)
date_in_six_months = date_in_six_months.strftime("%Y-%m-%d")

#
now_time = dt.datetime.now().strftime("%X")

city = sheety_data[0]['iataCode']
amadeus_token = flight_search.get_token()

amadeus_flight_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

amadeus_flight_headers = {
    "Authorization": f"Bearer {amadeus_token}"
}
amadeus_flight_params = {
    "originLocationCode": ORIGIN_IATA_CODE,
    "destinationLocationCode": "PAR",
    "departureDate": tomorrow_date,
    "returnDate": date_in_six_months,
    "adults": 1,
    "nonStop": "true",
    "currencyCode": "GBP",
    "max": 10,
}
amadeus_flight_response = requests.get(
    amadeus_flight_url,
    params=amadeus_flight_params,
    headers=amadeus_flight_headers
)
amadeus_flight_response.raise_for_status()
if amadeus_flight_response.status_code == 401:
    print("renewing token")
    flight_search.get_token()
amadeus_flight_data = amadeus_flight_response.json()
pprint.pprint(amadeus_flight_data)
