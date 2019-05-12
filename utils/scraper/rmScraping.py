import requests
from firebase import firebase
from bs4 import BeautifulSoup
from csv import writer

ref = firebase.FirebaseApplication('https://sourcedpropertygroup.firebaseio.com/', None)

rightMove_url = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E399&insId=1&radius=0.0&minPrice=&maxPrice=350000&minBedrooms=&maxBedrooms=&displayPropertyType=houses&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'
response = requests.get(rightMove_url)
soup = BeautifulSoup(response.text, "html.parser")
posts = soup.find_all('div', class_="propertyCard")

for post in posts:
    price = post.find(class_="propertyCard-priceValue").get_text().replace('\n','')
    title = post.find(class_="propertyCard-title").get_text().replace('\n','')
    address = post.find(class_="propertyCard-address").get_text().replace('\n','')
    addedOrReduced = post.find(class_="propertyCard-contactsAddedOrReduced").get_text().replace('\n','')
    
    data = {
        'Title': title,
        'Price': price,
        'Address': address,
        'AddedOrReduced': addedOrReduced
    }

    link = post.find(class_="propertyCard-link").get_text().replace('\n', '')
    ref.post('/myTestDate', data)

    
        