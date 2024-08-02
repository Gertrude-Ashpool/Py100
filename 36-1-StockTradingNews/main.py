import requests
import os
import datetime as dt
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
DELTA_MAX = 3

AV_Endpoint = 'https://www.alphavantage.co/query'
NewsApi_Endpoint = 'https://newsapi.org/v2/everything'

# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def stock_movement():
    # Alpha Vantage API details
    av_endpoint = AV_Endpoint
    av_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": os.environ.get("AV_API_KEY")
    }

    # get stock price JSON data from Alpha Vantage
    stock_response = requests.get(av_endpoint, params=av_parameters)
    stock_response.raise_for_status()
    stock_data = stock_response.json()

    # date wrangling to set variables
    date_today = str(dt.date.today())
    date_yesterday = str(dt.date.today() - dt.timedelta(days=1))
    date_before_yesterday = str(dt.date.today() - dt.timedelta(days=2))

    # filter data from Alpha Vantage down to relevant closing prices
    yesterdays_closing = float(stock_data['Time Series (Daily)'][date_yesterday]['4. close'])
    # print(yesterdays_closing)
    day_before_yesterdays_closing = float(stock_data['Time Series (Daily)'][date_before_yesterday]['4. close'])
    # print(day_before_yesterdays_closing)

    # calculate delta
    price_delta = yesterdays_closing - day_before_yesterdays_closing
    # print(delta)
    delta_percent = price_delta / (day_before_yesterdays_closing / 100)
    # print(delta_percent)
    return round(delta_percent,2)


def up_or_down(delta):
    if delta >= 0:
        return "up 🔼"
    if delta < 0:
        return "down 🔽"


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# News API call
def news_brief():
    api_endpoint = NewsApi_Endpoint
    parameters = {
        "q": "Tesla Inc",
        "from": str(dt.date.today() - dt.timedelta(days=2)),
        "to": str(dt.date.today() - dt.timedelta(days=1)),
        "sortBy": "relevancy",
        "pageSize": 3,
        "apiKey": os.environ.get("NEWS_API_KEY"),
    }

    # get stock price JSON data from Alpha Vantage
    news_response = requests.get(api_endpoint, params=parameters)
    news_response.raise_for_status()
    news_data = news_response.json()

    news_brief = {}

    for article in news_data['articles']:
        news_brief.update({article['title']: article['description']})
    return news_brief

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


def send_sms(message_body):
    account_sid = os.environ.get("TWILIO_SID")
    auth_token = os.environ.get("TWILIO_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=os.environ.get("TWILIO_NUMBER"),
        body=message_body,
        to=os.environ.get("MY_NUMBER")
    )

    print(message.status)


# get stock movement from alpha vantage
delta = stock_movement()

# set delta constant for testing
# delta = 4.25

if abs(delta) > DELTA_MAX:
    news_articles = news_brief()
    for headline, brief in news_articles.items():
        send_sms(f"{STOCK}: {up_or_down(delta)}{delta}%\nHeadline: {headline}\nBrief: {brief}")

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

