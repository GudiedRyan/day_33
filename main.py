from bs4 import BeautifulSoup
import requests
import smtplib
import os
import lxml

username = "yesmanvong@gmail.com"
password = os.environ["yesmanvongpass"]

url = "https://www.amazon.com/Instant-One-Touch-Multi-Use-Programmable-Pressure/dp/B07RCNHTLS/ref=dp_fod_2?pd_rd_i=B07RCNHTLS&psc=1"

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37"
}

response = requests.get(url=url, headers=headers)

product_text = response.text

soup = BeautifulSoup(markup=product_text, features="lxml")

price_soup = soup.find(name="span", id="priceblock_ourprice").getText()
price = price_soup.split("$")[1]

def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(
            from_addr=username,
            to_addrs="gudiedryan@gmail.com",
            msg=f"Subject: Sale!\n\nThe product you're interested in is currently only ${price}! Check it out here: {url}"
        )

if float(price) < 100:
    send_email()