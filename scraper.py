from bs4 import BeautifulSoup
import requests
import pandas as pd
from geopy.geocoders import Nominatim

def scrape(url, city=""):
    wiki_url = url

    response = requests.get(wiki_url)
    soup = BeautifulSoup(response.text,'lxml')

    synonyms = ['Name','Building','Building[2]','Structure','Building Name']

    building_list = soup.find_all('table', attrs={'class': "wikitable sortable"})

    df = pd.DataFrame()  # Initialize as an empty DataFrame
    dfs = []
    found = None

    for synonym in synonyms:
        try:
            temp_df = pd.read_html(str(building_list[0]))[0].loc[:,synonym]
            if found is None:
                df = temp_df
            found = synonym
            break  # Break the loop if a valid column is found
        except:
            pass

    for ind in range(1, len(building_list)):
        try:
            additional_df = pd.read_html(str(building_list[ind]))[0].loc[:,found]
            dfs.append(additional_df)
        except:
            pass
    
    df = pd.concat([df] + dfs, ignore_index=True)

    if df.empty:
        return False
    geolocator = Nominatim(user_agent='unipath',timeout=None)
    file = open("building.csv", "w")
    file.write("Building,Latitude,Longitude\n")
    try:
        for item in df[found]:
            building = item
            address=geolocator.geocode(building + " " + city)
            if address is not None:
                file.write(building + "," + str(address.latitude) + "," + str(address.longitude)+ "\n")
    except:
        for item in df:
            building = item
            address=geolocator.geocode(building + " " + city)
            if address is not None:
                file.write(building + "," + str(address.latitude) + "," + str(address.longitude)+ "\n")
    file.close()
    return True