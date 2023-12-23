import networkx as nx
import pandas as pd
from geopy import distance

class Map:
    def __init__(self) -> None:
        self.map = self.graphMaker("building.csv")
        self.mst = nx.minimum_spanning_tree(self.map)
        self.maxst = nx.maximum_spanning_tree(self.map)
    
    def getMap(self):
        return self.map

    def getMST(self):
        return self.mst
    
    def getMaxST(self):
        return self.maxst

    def graphMaker(self, filename):
        visited = set()
        data = pd.read_csv(filename,sep=',', encoding='windows-1252')
        map = nx.Graph()
        for index, data1 in data.iterrows():
            for index2, data2 in data.iterrows():
                if data1.at["Building"] == data2.at["Building"]:
                    continue
                if tuple([data1["Building"],data2["Building"]]) in visited:
                    continue
                map.add_edge(data1.at["Building"],data2.at["Building"], weight=distance.distance((data1.at["Latitude"], data1.at["Longitude"]),(data2.at["Latitude"], data2.at["Longitude"])).miles)
                visited.add(tuple([data1.at["Building"],data2.at["Building"]]))
            nx.set_node_attributes(map,{data1.at["Building"]: {'Latitude': data1.at["Latitude"], 'Longitude': data1.at["Longitude"]}})
        return map
