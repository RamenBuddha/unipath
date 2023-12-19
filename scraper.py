from bs4 import BeautifulSoup
from IPython.display import display
import requests
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
from geopy.geocoders import Nominatim

wiki_url = 'https://en.wikipedia.org/wiki/List_of_University_of_Florida_buildings'

response = requests.get(wiki_url)
soup = BeautifulSoup(response.text,'html.parser')

building_list = soup.find('table', attrs={'class': "wikitable sortable"})
df = pd.read_html(str(building_list))[0].loc[:,'Building[2]']

load_dotenv(find_dotenv())

geolocator = Nominatim(user_agent='unipath',timeout=None)

file = open("building.csv", "w")
file.write("Building,Latitude,Longitude\n")
for item in df:
    building = item + " Gainesville Florida"
    address=geolocator.geocode(building)
    if address is not None:
        file.write(building + "," + str(address.latitude) + "," + str(address.longitude)+ "\n")
file.close()
