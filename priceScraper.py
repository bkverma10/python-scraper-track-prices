from bs4 import BeautifulSoup
from selenium  import webdriver


driver = webdriver.Chrome('/Users/bharatverma/Documents/GitHub/python-scraper-track-prices/chromedriver')
driver.get('https://www.amazon.com/NIKE-Revolution-Running-Black-Cool-Regular/dp/B06XKLCKHK/ref=sr_1_3?keywords=nike%2Bshoes%2Bmen&qid=1562706205&s=gateway&sprefix=nike&sr=8-3&th=1&psc=1')
soup = BeautifulSoup(driver.page_source,"lxml")


title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = price[1:6]
print(converted_price)
print(title.strip())
driver.quit()
