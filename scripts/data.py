import requests
import pandas as pd
from arcgis.gis import GIS
import json



## property data goes here
url = 'https://opendata.vancouver.ca/api/records/1.0/search/?dataset=property-parcel-polygons&q=&rows=10000&facet=streetname'

response = requests.get(url)
data = response.json()
df = pd.DataFrame(data["records"])

## Clean data

gis = GIS()
# for index, row in df.iterrows():
    
#     print(row)
#     print()
    
    # Use the latitude and longitude from the data to search for satellite imagery
#     search_result = gis.content.search("latitude:"+row["latitude"]+" AND longitude:"+row["longitude"], item_type = "Imagery Layer")
#     # Access the image and metadata
#     image = search_result[0]
#     image_url = image.url
#     image_metadata = image.get_data()
#     # Add the image_url and metadata to the dataframe
#     df.at[index, 'image_url'] = image_url
#     df.at[index, 'image_metadata'] = image_metadata


#Code below is to get 10000 records from the API and save them to a json file

# with open("tamim.json", "w") as f:
#     json.dump(data, f, indent=4)


#Code below is to find the number of unique civic numbers in the data
# civics = {}

# for record in data["records"]:
    
#     fields = record["fields"]
    
#     if "civic_number" in fields:
#         if fields["civic_number"] not in civics:
#             civics[fields["civic_number"]] = 1
#         else:
#             civics[fields["civic_number"]] += 1
        
    
    
# print(data["records"][6000]["fields"]["civic_number"])
            
# print(len(civics.keys()))


#Code below is to find the number of lists of coordinates in every record and count them
#Also sorts the dictionary by the number of coordinates in the list

# coord_lens = {}

# for record in data["records"]:
    
#     coords = record["fields"]["geom"]["coordinates"]
    
#     length = len(coords[0])
    
#     if not str(length) in coord_lens:
#         coord_lens[str(length)] = 1
#     else:
#         coord_lens[str(length)] += 1

# coord_lens = dict(sorted(coord_lens.items(), key=lambda item: int(item[0])))

# for key, value in coord_lens.items():
#     print(f"KEY: {key} VALUE: {value}")