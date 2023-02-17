import requests
import pandas as pd
from arcgis.gis import GIS

## property data goes here
url = 'https://opendata.vancouver.ca/api/records/1.0/search/?dataset=storefronts-inventory&q=&facet=retail_category&facet=year_recorded&facet=geo_local_area&facet=geo_m'

response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)

## Clean data

gis = GIS()
for index, row in df.iterrows():
    # Use the latitude and longitude from the data to search for satellite imagery
    search_result = gis.content.search("latitude:"+row["latitude"]+" AND longitude:"+row["longitude"], item_type = "Imagery Layer")
    # Access the image and metadata
    image = search_result[0]
    image_url = image.url
    image_metadata = image.get_data()
    # Add the image_url and metadata to the dataframe
    df.at[index, 'image_url'] = image_url
    df.at[index, 'image_metadata'] = image_metadata

print(df)