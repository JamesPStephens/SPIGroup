import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get
('https://www.rightmove.co.uk/property-for-sale/property-81114080.html')

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.body.h1)

# .get_text()

el = soup.find(class_="item")


print(el)