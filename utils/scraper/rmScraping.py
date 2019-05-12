import requests
from bs4 import BeautifulSoup
from csv import writer

rightMove_url = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E87490&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'
response = requests.get(rightMove_url)
soup = BeautifulSoup(response.text, "html.parser")
posts = soup.find_all('div', class_="propertyCard")

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title, Price, Address, AddedOrReduced', 'Link']
    csv_writer.writerow(headers)


    for post in posts:
        price = post.find(class_="propertyCard-priceValue").get_text().replace('\n', '')
        title = post.find(class_="propertyCard-title").get_text().replace('\n', '')
        address = post.find(class_="propertyCard-address").get_text().replace('\n', '')
        addedOrReduced = post.find(class_="propertyCard-contactsAddedOrReduced").get_text().replace('\n', '')
        link = post.find(class_="propertyCard-link").get_text().replace('\n', '')
        csv_writer.writerow([title, price, address, addedOrReduced, link])
        