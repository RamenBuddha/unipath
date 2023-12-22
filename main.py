import folium
import sys
import io
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from networkx.algorithms.tree.mst import minimum_spanning_tree
from nodes import Map

def main(argv):
    if (len(argv) > 2):
        g = Map().getMap()
        map = folium.Map(location=[g.nodes[argv[1]]['Latitude'],g.nodes[argv[1]]['Longitude']],zoom_start=15)
        folium.Marker(location=[g.nodes[argv[1]]['Latitude'],g.nodes[argv[1]]['Longitude']],
                            popup="Name: " + argv[1] + "\n" + "Coordinates: " + str(g.nodes[argv[1]]['Latitude']) + '\n' + str(g.nodes[argv[1]]['Longitude'])).add_to(map)
        folium.Marker(location=[g.nodes[argv[2]]['Latitude'],g.nodes[argv[2]]['Longitude']],
                            popup="Name: " + argv[2] + "\n" + "Coordinates: " + str(g.nodes[argv[2]]['Latitude']) + '\n' + str(g.nodes[argv[2]]['Longitude'])).add_to(map)
        folium.PolyLine(locations=[(g.nodes[argv[1]]['Latitude'],g.nodes[argv[1]]['Longitude']),(g.nodes[argv[2]]['Latitude'],g.nodes[argv[2]]['Longitude'])],
                                tooltip="Distance: " + str(round(g[argv[1]][argv[2]]['weight'],2)) + " miles\n" + f"ETA Walking: {round(g[argv[1]][argv[2]]['weight']/3 * 60,2)} minutes").add_to(map)
    else:
        if argv[1] == "mst":
            g = Map().getMST()
        elif argv[1] == "maxst":
            g = Map().getMaxST()
        once = True
        for first, second, attr in g.edges(data = True):
            if once:
                map = folium.Map(location=[g.nodes[first]['Latitude'],g.nodes[first]['Longitude']],zoom_start=15)
                once = False
            folium.Marker(location=[g.nodes[first]['Latitude'],g.nodes[first]['Longitude']],
                        popup="Name: " + first + "\n" + "Coordinates: " + str(g.nodes[first]['Latitude']) + '\n' + str(g.nodes[first]['Longitude'])).add_to(map)
            folium.Marker(location=[g.nodes[second]['Latitude'],g.nodes[second]['Longitude']],
                        popup="Name: " + second + "\n" + "Coordinates: " + str(g.nodes[second]['Latitude']) + '\n' + str(g.nodes[second]['Longitude'])).add_to(map)
            folium.PolyLine(locations=[(g.nodes[first]['Latitude'],g.nodes[first]['Longitude']),(g.nodes[second]['Latitude'],g.nodes[second]['Longitude'])],
                            tooltip="Distance: " + str(round(attr['weight'],2)) + " miles\n" + f"ETA Walking: {round(attr['weight']/3 * 60,2)} minutes").add_to(map)
    
        
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



