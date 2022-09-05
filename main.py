from bs4 import BeautifulSoup
import requests
from random import randint
from time import sleep


def getCarLinkAndImage():

    carTitle = soup.find('h2', class_='e1b25f6f12 ooa-1mgjl0z-Text eu5v0x0')
    #print(carTitle.a['href'])

    with open(f'Document.txt', 'w') as f:
      f.write(carTitle.a['href'])

    #g = open('Document.txt', "r")
    #print(g.read())


    sleep(randint(3, 7))


if __name__ == '__main__':

    for i in range(0, 1):
        url = 'https://www.autovit.ro/autoturisme?page='
        req = requests.get(url + str(i)).text
        soup = BeautifulSoup(req, 'lxml')

        getCarLinkAndImage()
