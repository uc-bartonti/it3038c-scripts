from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://www.designbyhumans.com/shop/t-shirt/men/super-mario-and-yoshi-stars/1187255/').content
soup = BeautifulSoup(r, "lxml")
##print(r)
##print(type(soup))
##print(soup.prettify()[:100])
##for link in soup.find_all('a'): print(link.get('href'))
##span = soup.find("a", {"aria-lable":})
currencyAmount = soup.find("span", {"class": "currency-amount"})
price = currencyAmount.text
shirtName = soup.find("h1", {"class": "detail-view-title"})
title = shirtName.text
print("The shirt name is %s with the price %s" %(title.strip(), price))
