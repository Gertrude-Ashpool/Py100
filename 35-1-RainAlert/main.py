import requests
from twilio.rest import Client

# Twilio.com credentials
account_sid = "account sid"
auth_token = "token"

# Open Weather Maps Credentials
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = "xxxx xxxx xxxx"

# lat/long of location to check
MY_LAT = 41.616756
MY_LNG = 41.636745

# Parameters for weather API call
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

# Get Weather data
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

# Create a slice of weatherdata to get the next twelve hours
next_twelve_hours = weather_data["hourly"][:12]

# Create a list of the next 12 weather condition codes
next_twelve_ids = [hour['weather'][0]['id'] for hour in next_twelve_hours]

will_rain = False

for id in next_twelve_ids:
    if int(id) < 700:
        will_rain = True

if will_rain:
    # Send SMS
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='Twilio number',
        body='Better bring a brolly, mate.☔️',
        to='Recipients phone number'
    )
    print(message.status)

# print("Better bring a brolly, mate.☔️")

