# Price Checking on Amazon.in

import requests
from bs4 import BeautifulSoup
import smtplib
import time, datetime


URL = 'https://www.amazon.in/'                  # Go to the site, search for the item and paste the complete URL here
headers = {"User-Agent": 'Mozilla'}             # Search 'my user agent' on Google and paste it completely inside the curly braces


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    title = soup.find(id="productTitle").text                           # Getting product's title
    # print(title.strip())

    price = soup.find(id="priceblock_ourprice").text                    # Getting product's price
    converted_price = float(price[2:5])                                 # Excluding the currency symbol, hence getting exact value we need
    print(today + ": " + str(converted_price))

    if converted_price <= 600:                                          # Value depends on your overall budget
        send_mail()

    return title


def send_mail():
    title = check_price()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    if now == datetime.datetime(2020, 2, 10):                           # (yyyy-mm-dd) format date; code will keep running till this date
        server.quit()

    else:
        server.login('mail-id', 'password')

        subject = "Price fell down: " + title.strip()
        body = 'Check the Amazon link: \n' \
                + URL
        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            'from_mail_id',
            'to_mail_id',
            msg
        )

        print("Email Sent!")
        server.close()


while True:
    now = datetime.datetime.now()
    today = now.strftime("%d%b-%H%M")
    # print(today)

    check_price()
    time.sleep(3600)                              # Will run the code every hour



