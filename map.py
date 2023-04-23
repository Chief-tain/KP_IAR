import re
import string
# import nltk
# import pymorphy2
import json
import folium
from folium import plugins, TileLayer
from folium import FeatureGroup
from folium.plugins import MarkerCluster
# from nltk.corpus import stopwords
from datetime import timedelta
from datetime import datetime
# from docx import Document
# from docx.shared import Pt
# from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
# from docx.shared import Mm
# from fuzzywuzzy import fuzz
import os

from DB_UK import Db

class MainMap:

    def map_creation(self, lon, lat):

        map = folium.Map(width=800,
                         height=980,
                         location=[lon, lat],
                         tiles='openstreetmap',
                         zoom_start=15,
                         min_zoom=5)

        plugins.Geocoder().add_to(map)

        fmtr = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
        plugins.MousePosition(
            position="topright",
            separator=" | ",
            prefix="Coordinates:",
            lat_formatter=fmtr,
            lng_formatter=fmtr).add_to(map)

        minimap = plugins.MiniMap()
        map.add_child(minimap)

        plugins.Fullscreen().add_to(map)

        plugins.MeasureControl(position='topright',
                               primary_length_unit='meters',
                               secondary_length_unit='miles',
                               primary_area_unit='sqmeters',
                               secondary_area_unit='acres').add_to(map)

        folium.TileLayer('Stamen Toner').add_to(map)
        folium.TileLayer('Stamen Terrain').add_to(map)
        folium.TileLayer('Stamen Watercolor').add_to(map)
        folium.TileLayer('openstreetmap').add_to(map)
        folium.TileLayer('cartodbpositron').add_to(map)
        folium.TileLayer('cartodbdark_matter').add_to(map)

        folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri',
            name='Esri Satellite',
            overlay=False,
            control=True
        ).add_to(map)

        plugins.Draw().add_to(map)
        folium.LayerControl().add_to(map)

        map_name = 'certain_map.html'
        map.save(map_name)

        with open(map_name, 'r', encoding="utf8") as f:
            self.html = f.read()

    def start_map_creation(self):

        start_map = folium.Map(width=800,
                         height=980,
                         location=[55, -4],
                         tiles='openstreetmap',
                         zoom_start=6,
                         min_zoom=5)

        plugins.Geocoder().add_to(start_map)

        fmtr = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
        plugins.MousePosition(
            position="topright",
            separator=" | ",
            prefix="Coordinates:",
            lat_formatter=fmtr,
            lng_formatter=fmtr).add_to(start_map)

        minimap = plugins.MiniMap()
        start_map.add_child(minimap)

        plugins.Fullscreen().add_to(start_map)

        plugins.MeasureControl(position='topright',
                               primary_length_unit='meters',
                               secondary_length_unit='miles',
                               primary_area_unit='sqmeters',
                               secondary_area_unit='acres').add_to(start_map)

        folium.TileLayer('Stamen Toner').add_to(start_map)
        folium.TileLayer('Stamen Terrain').add_to(start_map)
        folium.TileLayer('Stamen Watercolor').add_to(start_map)
        folium.TileLayer('openstreetmap').add_to(start_map)
        folium.TileLayer('cartodbpositron').add_to(start_map)
        folium.TileLayer('cartodbdark_matter').add_to(start_map)

        folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri',
            name='Esri Satellite',
            overlay=False,
            control=True
        ).add_to(start_map)

        plugins.Draw().add_to(start_map)
        folium.LayerControl().add_to(start_map)

        db = Db()

        records_vmb = db.read_db_vmb()
        for record in records_vmb:
            pushpin = folium.features.CustomIcon('ВМБ.png', icon_size=(30,30))
            folium.Marker(location=[record[2], record[3]],
                              popup=record[1],
                              tooltip=['ВМБ', record[1]],
                              icon=pushpin).add_to(start_map)
            
        records_avb = db.read_db_avb()
        for record in records_avb:
            pushpin = folium.features.CustomIcon('АвБ.png', icon_size=(30,30))
            folium.Marker(location=[record[2], record[3]],
                              popup=record[1],
                              tooltip=['АвБ', record[1]],
                              icon=pushpin).add_to(start_map)
            
        records_vg = db.read_db_vg()
        for record in records_vg:
            pushpin = folium.features.CustomIcon('ВГ.png', icon_size=(30,30))
            folium.Marker(location=[record[2], record[3]],
                              popup=record[1],
                              tooltip=['ВГ', record[1]],
                              icon=pushpin).add_to(start_map)

        map_name = 'total_map.html'
        start_map.save(map_name)
        # os.startfile(map_name)


# total_map = MainMap()
# total_map.start_map_creation()