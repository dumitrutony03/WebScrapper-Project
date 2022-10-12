from bs4 import BeautifulSoup
import requests
from random import randint
from time import sleep
import mysql.connector
import json

def getCarDetails():

    # Get the link of the car from the list of cars,
    carLink = car.find('h2', class_='e1b25f6f12 ooa-1mgjl0z-Text eu5v0x0')

    sleep(randint(3,7))

    #print(carLink.a['href'])
    #return

    # Request the link and navigate to the page where we can SCRAPE details about the car, individual
    urlCarLink = carLink.a['href']
    reqCarTitle = requests.get(urlCarLink).text
    soupCarTitle = BeautifulSoup(reqCarTitle, 'lxml')
    sleep(randint(3, 7))

    #print(urlCarLink)
    #return

    # Car's Name
    carName = soupCarTitle.find('span', class_='offer-title big-text fake-title')
    #print(f"Car Name: {carName.text.strip()}")
    sleep(randint(3, 7))

    carPrice = soupCarTitle.find('span', class_='offer-price__number')
    #print(f"Car Price: {carPrice.text.replace(' ', '').strip()}")
    sleep(randint(3, 7))

    #Save details about the car's ad
    carNameMySql = carName.text.strip()
    carPriceMySql = carPrice.text.replace(' ', '').strip()

    dictionary = {
         "carLink": urlCarLink,
         "carName": carNameMySql,
         "carPrice": carPriceMySql
    }

    # Get the Car's Ad features
    carFeaturesLI = soupCarTitle.find_all('li', class_='offer-params__item')
    sleep(randint(3, 7))
    
    for carFeatureLI in carFeaturesLI:
        carFeatureSpan = carFeatureLI.find("span", class_="offer-params__label")

        #print(carFeatureSpan.text.strip())

        carFeatureDiv = carFeatureLI.find('div', class_='offer-params__value')
        sleep(randint(3, 7))
        
        if carFeatureDiv.findChild() is not None:
            carFeatureDiv = carFeatureLI.find('a', class_='offer-params__link')
        else:
            carFeatureDiv = carFeatureLI.find('div', class_='offer-params__value')

        carDetails = carFeatureSpan.text.strip()
        carFeatures = carFeatureDiv.text.strip()

        dictionary.update({carDetails: carFeatures})

        sleep(randint(3, 7))

    mainDictionary.update({ct: dictionary})

    # Serializing json
    json_object = json.dumps(mainDictionary, indent=4)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

    print(mainDictionary)
    
    # This helps us not to get banned from the Website that we are Scrapping
    #sleep(randint(3, 7))

if __name__ == '__main__':

    ct = 0
    mainDictionary = {}

    # Taking Website's multiple pages
    for i in range(0, 1):
        url = 'https://www.autovit.ro/autoturisme?page='
        req = requests.get(url + str(i)).text
        soup = BeautifulSoup(req, 'lxml')

        carsList = soup.find_all("article", class_="ooa-1wi71qz e1b25f6f18")

        #print(carsList)

        for car in carsList:
            ct += 1

            print(car.text)
            getCarDetails()
            print("\n")
