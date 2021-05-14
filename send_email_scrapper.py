import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_2?dchild=1&keywords=sony+a7iii&qid=1613457955&sr=8-2'

#URL = 'https://www.c4dcafe.com/ipb/discover/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if converted_price < 1.700:
        send_mail()

    print (soup.prettify()) 



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('btfiverr05@gmail.com', 'XXXX')
    subject = 'Price fell down'
    body = 'Check the amazon link'
    msg = f"Subject: {subject}\n\n {body}"
    server.sendmail(
        'btfiverr05@gmail.com',
        'bentraje@gmail.com',
        msg
    )

    print ("Hey EMAIL HAS BEEN SENT")

    server.quit()

# while (True):
#     check_price()
#     time.sleep(60)

send_mail()