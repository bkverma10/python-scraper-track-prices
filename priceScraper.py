from selenium  import webdriver
import smtplib
from bs4 import BeautifulSoup
import config
import time

driver = webdriver.Chrome(config.chromeDriver)
driver.get(config.priceScraperURL)

def check_price():
    soup = BeautifulSoup(driver.page_source,"lxml")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])

    if(converted_price < 40):
        send_mail()

    print(converted_price)
    print(title.strip())
    driver.quit()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.connect('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(config.mailFromAddress, config.mailFromPassword)

    subject = 'Email from Python WebScraper'
    body = 'Success'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        config.mailFromAddress,
        config.mailToAddress,
        msg
    )

    print('Hey Email has been sent!!!')
    server.quit()

while(True):
    check_price()
    time.sleep(60*60*24)


