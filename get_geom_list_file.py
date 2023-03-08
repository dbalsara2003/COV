import requests
import pandas as pd
import json

## property data goes here
url = 'https://opendata.vancouver.ca/api/records/1.0/search/?dataset=property-parcel-polygons&q=&rows=10000&facet=streetname'

response = requests.get(url)
data = response.json()
df = pd.DataFrame(data["records"])

## Clean data


coords = []
for record in data["records"]:
    coords.append(record["fields"]["geom"]["coordinates"][0])

coordinates = {"coordinates": coords}

with open("coordinates.json", mode="r+") as p:
    json.dump(coordinates, p, indent=4)

url = "https://opendata.vancouver.ca/api/records/1.0/search/?dataset=storefronts-inventory&q=&rows=10000&facet=geo_local_area"

response = requests.get(url)
data = response.json()
df = pd.DataFrame(data["records"])
centroids = []
for i in df['geometry']:
    centroids.append(i['coordinates'])

centroid = {"centroid": centroids}
with open("centroids.json", "w+") as p:
    json.dump(centroid, p, indent=4)