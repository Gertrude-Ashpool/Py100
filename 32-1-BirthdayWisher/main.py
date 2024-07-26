import smtplib
import datetime as dt
import random
import pandas as pd
import os

# Put your email login and password here here
MY_EMAIL = "my.email@mail.com"
PASSWORD = "password"
SMTP_SERVER = "smtp.host.com"


def send_birthday_email(recipient_name, recipient_email):
    random_letter = f"letter_templates/{random.choice(os.listdir("letter_templates"))}"
    with open(random_letter) as random_letter:
        template = random_letter.read()
        message = template.replace('[NAME]', recipient_name)
        with smtplib.SMTP(SMTP_SERVER) as connection:
            # Enable TLS encryption
            connection.starttls()
            # Login / pass as above
            connection.login(user=MY_EMAIL, password=PASSWORD)
            # Send a message
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=recipient_email,
                # Body separated form subject by two line breaks
                msg=f"Subject:Happy Birthday!\n\n{message}"
            )


# get current date
now = dt.datetime.now()

# import birthday DB
with open("birthdays.csv") as birthdays_file:
    birthdays = pd.read_csv(birthdays_file)
    birthday_dict = birthdays.to_dict(orient="records")
    # Extract entries with today's day and month
    birthdays_today = [
        entry for entry in birthday_dict
        if entry['month'] == now.month
        and entry['day'] == now.day
    ]
    # call send email for each entry in today's birthday list
    for birthday in birthdays_today:
        send_birthday_email(birthday['name'], birthday['email'])
