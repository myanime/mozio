import json
import traceback
from geojson import Polygon

class GeojsonParser:
    def __init__(self, data):
        self.location =  data['location']
        self.data = data
    def set(self):
        try:
            #crimea = Polygon([[(34.15, 44.48), (34.15, 44.49), (34.17, 44.49), (34.17, 44.48), (34.15, 44.48)]])
            c1 = tuple(self.location[0:2])
            c2 = tuple(self.location[2:4])
            c3 = tuple(self.location[4:6])
            c4 = tuple(self.location[6:8])
            list_to_polygon = Polygon([[c1,c2,c3,c4]])
            
            #Updates the Response data
            self.data['geojson_object'] = list_to_polygon
            return self.data
        except:
            #Returns Error message in JSON output
            self.data['geojson_object'] = "Error"

            #Server side traceback 
            traceback.print_exc()
            return self.data
