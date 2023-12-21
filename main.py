import folium
import sys
import io
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from networkx.algorithms.tree.mst import minimum_spanning_tree
from nodes import Map

def main(argv):
    map = folium.Map(location=[29.6520,-82.3250])
    if (len(argv) > 2):
        g = Map().getMap()
        folium.Marker(location=[g.nodes[argv[1]]['Latitude'],g.nodes[argv[1]]['Longitude']],
                            popup=argv[1] + "\n" + str(g.nodes[argv[1]]['Latitude']) + '\n' + str(g.nodes[argv[1]]['Longitude'])).add_to(map)
        folium.Marker(location=[g.nodes[argv[2]]['Latitude'],g.nodes[argv[2]]['Longitude']],
                            popup=argv[2] + "\n" + str(g.nodes[argv[2]]['Latitude']) + '\n' + str(g.nodes[argv[2]]['Longitude'])).add_to(map)
        folium.PolyLine(locations=[(g.nodes[argv[1]]['Latitude'],g.nodes[argv[1]]['Longitude']),(g.nodes[argv[2]]['Latitude'],g.nodes[argv[2]]['Longitude'])],
                                tooltip=str(g[argv[1]][argv[2]]['weight']) + " miles").add_to(map)
    else:
        if argv[1] == "mst":
            g = Map().getMST()
        elif argv[1] == "maxst":
            g = Map().getMaxST()
        for first, second, attr in g.edges(data = True):
                folium.Marker(location=[g.nodes[first]['Latitude'],g.nodes[first]['Longitude']],
                            popup=first + "\n" + str(g.nodes[first]['Latitude']) + '\n' + str(g.nodes[first]['Longitude'])).add_to(map)
                
                folium.Marker(location=[g.nodes[second]['Latitude'],g.nodes[second]['Longitude']],
                            popup=second + "\n" + str(g.nodes[second]['Latitude']) + '\n' + str(g.nodes[second]['Longitude'])).add_to(map)
                folium.PolyLine(locations=[(g.nodes[first]['Latitude'],g.nodes[first]['Longitude']),(g.nodes[second]['Latitude'],g.nodes[second]['Longitude'])],
                                tooltip=str(attr['weight']) + " miles").add_to(map)
        
    app = QApplication(sys.argv)
    data = io.BytesIO()
    map.save(data, close_file=False)
    map.save("map.html")

    window = QWebEngineView()
    window.setHtml(data.getvalue().decode())
    window.resize(1600,1200)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv)



