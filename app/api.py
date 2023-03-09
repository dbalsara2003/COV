import pandas as pd
import json
import requests
from model import *

### API LINK
url = 'https://opendata.vancouver.ca/api/records/1.0/search/?dataset=storefronts-inventory&q=&lang=en&rows=1500&facet=retail_category&facet=year_recorded&facet=geo_local_area'

### READING JSON DATA
res = requests.get(url)
data = json.loads(res.text)

### LOOKING SPECIFICALLY AT THE RECORDS SECTION
records = data['records']
ROWS = data['parameters']['rows']

### CREATING AN EMPTY LIST OF STORES
store_list = Stores_list()

### SETTING THE EMPTY LIST EQUAL TO A LIST OF STORES 
### WITH THE DATA FROM THE RECORDS SECTION

store_list.stores = [Store(record['datasetid'], 
record['recordid'],
record['fields']['geom']['coordinates'],
record['fields']['unit'],
record['fields']['geo_point_2d'],
record['fields']['year_recorded'],
record['fields']['id'],
record['fields']['street_name_parcel'],
record['fields']['retail_category'],
record['fields']['civic_number_parcel'],
record['fields']['business_name'],
record['fields']['geo_local_area'],
record['geometry']['type'],
record['record_timestamp']
) for record in records]

### PRINTING THE STORE LIST
# print(store_list)

### TESTING TO SEE IF ALL ENTRIES ARE SAVED BY 
### PRINTING THE LENGTH OF THE LIST AND COMPARING IT TO THE ROWS PARAMETER
print(len(store_list.stores) == ROWS)

### TESTING THE GET_BY_NAME METHOD
print(len(store_list.get_by_name('Starbucks')))

### TESTING THE GET_BY_CATEGORY METHOD
print(len(store_list.get_by_category('Convenience Goods')))

### TESTING THE GET_BY_AREA METHOD
print(len(store_list.get_by_area('Kits')))

st = store_list.get_by_name('Starbucks')

print(st[0])
