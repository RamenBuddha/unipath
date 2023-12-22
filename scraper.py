from bs4 import BeautifulSoup
import requests
import pandas as pd
from geopy.geocoders import Nominatim

def scrape(url, city=""):
    wiki_url = url
    print(wiki_url)

    response = requests.get(wiki_url)
    soup = BeautifulSoup(response.text,'html.parser')

    synonyms = ['Building','Building[2]','Structure','Name']

    building_list = soup.find('table', attrs={'class': "wikitable sortable"})

    df = None

    for synonym in synonyms:
        try:
            df = pd.read_html(str(building_list))[0].loc[:,synonym]
            if df is not None:
                break
        except:
            pass

    if df is None:
        return False
    geolocator = Nominatim(user_agent='unipath',timeout=None)
    file = open("building.csv", "w")
    file.write("Building,Latitude,Longitude\n")
    for item in df:
        building = item
        address=geolocator.geocode(building + " " + city)
        if address is not None:
            file.write(building + "," + str(address.latitude) + "," + str(address.longitude)+ "\n")
    file.close()
    return True
