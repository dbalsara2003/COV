from arcgis.gis import GIS, ItemProperties

gis = GIS()
map = gis.map("British Columbia, Canada", zoomlevel=5)
map.add_layer({"type":"FeatureLayer",
                "url":"https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/Canada_Provinces_Territories_simple/FeatureServer/0",
                "title":"Canadian Provinces"})
# item_properties = ItemProperties({"type":"Point", "spatialReference":{"wkid":4326}, "x": -75.70, "y": 45.42})
# marker = gis.content.add("My marker", item_properties)
# map.add_layer(marker)
map
