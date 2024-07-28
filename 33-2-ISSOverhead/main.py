import requests
from datetime import datetime
import pytz
import smtplib
import time

BNE_LAT = -27.469770
BNE_LNG = 153.025131

my_email = "my.mail@mail.com"
password = "mail password"
smpt_server = "smtp.domain.com"
mail_recipient = "your.email@mail.com"


def iss_is_close():
    min_lat = float(BNE_LAT - 5)
    max_lat = float(BNE_LAT + 5)
    min_lng = float(BNE_LNG - 5)
    max_lng = float(BNE_LNG + 5)
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if min_lat <= iss_latitude <= max_lat and min_lng <= iss_longitude <= max_lng:
        return True


def is_dark():
    parameters = {
        "lat": BNE_LAT,
        "lng": BNE_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(pytz.utc)
    hour_now = time_now.hour
    if sunset <= hour_now or sunrise >= hour_now:
        return True

while True:
    time.sleep(60)
    if iss_is_close() and is_dark():
        with smtplib.SMTP(smpt_server) as connection:
            # Enable TLS encryption
            connection.starttls()
            # Login / pass as above
            connection.login(user=my_email, password=password)
            # Send a message
            connection.sendmail(
                from_addr=my_email,
                to_addrs=mail_recipient,
                # Body separated form subject by two line breaks
                msg=f"Subject:Look Up!\n\nISS Overhead"
            )
