import json
import requests
import pandas as pd
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

## property data goes here
url = 'https://opendata.vancouver.ca/api/records/1.0/search/?dataset=storefronts-inventory&q=&lang=en&rows=1500&facet=retail_category&facet=year_recorded&facet=geo_local_area'

response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)

## Clean data
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)


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

# Create the model
x = df[['number_of_rooms']]
y = df[['floor_area']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
df_pred = pd.DataFrame({'actual_floor_area': y_test, 'predicted_floor_area': y_pred})

# Create feature layer from the estimated floor area data
feature_layer = FeatureLayer.from_dataframe(df_pred)
# Overlay the feature layer on the satellite imagery
map1 = gis.map("Vancouver")
map1.add_layer(feature_layer)
map1.add_layer(image)
