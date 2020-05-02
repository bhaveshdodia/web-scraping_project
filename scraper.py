import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Magnum-Flat-Respirator-NIOSH-Certification/dp/B085LK14ZX/ref=sr_1_2?dchild=1&keywords=N95+Mask&qid=1588345326&s=industrial&sr=1-2'

headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

def check_price():

    page = requests.get(URL,headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')

    price = soup.find(id='priceblock_ourprice').get_text().strip()
    converted_price = int(price[1:5])

    if (converted_price < 850):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('bhaveshdodia1@gmail.com','orevzsqbbhwtkhmw')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Magnum-Flat-Respirator-NIOSH-Certification/dp/B085LK14ZX/ref=sr_1_2?dchild=1&keywords=N95+Mask&qid=1588345326&s=industrial&sr=1-2'

    msg = 'Subject: %s \n %s '%(subject, body)

    server.sendmail('bhaveshdodia1@gmail.com','nups.das@gmail.com',msg)

    print('Email sent')

    server.quit()

while(True):
    check_price()
    #time.sleep(60)