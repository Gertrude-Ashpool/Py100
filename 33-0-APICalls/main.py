import requests
from datetime import datetime

# define constants for our location
BNE_LAT = -27.469770
BNE_LNG = 153.025131

# # get the current position of the iss space station
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# # will return an exception and error code for anything but 200 / success
# response.raise_for_status()
#
# # lets pull the actual data
# data = response.json()
#
# # extract relevant data
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

# format the parameters and name the keys as required by the API
parameters = {
    "lat": BNE_LAT,
    "lng": BNE_LNG,
    "formatted": 0,
}

# pass the parameters along with the request to the API
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(sunset)
print(sunrise)



time_now = datetime.now()
print(time_now)



