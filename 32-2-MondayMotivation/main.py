import datetime as dt
import random
import smtplib

# Put your email login and password here
my_email = "my.mail@mail.com"
password = "mail password"
smpt_server = "smtp.domain.com"
mail_recipient = "your.email@mail.com"

now = dt.datetime.now()
day_of_the_week = now.weekday()


if day_of_the_week == 4:
    try:
        with open("quotes.txt") as quotes_file:
            quotes_list = quotes_file.readlines()
            quote_of_the_day = random.choice(quotes_list)
    except FileNotFoundError as error_message:
        print(error_message)

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
            msg=f"Subject:Quote of the Day\n\n{quote_of_the_day}"
        )
