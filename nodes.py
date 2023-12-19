import networkx as nx
import pandas as pd
from geopy import distance

def graphMaker(filename):
    data = pd.read_csv('building.csv',sep=',')
    map = nx.Graph()
    for index, data1 in data.iterrows():
        for index2, data2 in data.iterrows():
            map.add_edge(data1.at["Building"],data2.at["Building"], weight=distance.distance((data1.at["Latitude"], data1.at["Longitude"]),(data2.at["Latitude"], data2.at["Longitude"])).miles)
    for first, second, attr in map.edges(data=True):
        print(f"{first} to {second} with weight {attr.get('weight')}")
