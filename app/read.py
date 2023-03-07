import pandas as pd
import chardet
from model import * 

file = 'sample_storefront_inventory.csv'

with open(file, 'rb') as f:
    enc = chardet.detect(f.read())

## ADD nrow = <any number you want to limit> (to limit the number of rows read in the parameters below)
df = pd.read_csv(file, encoding = enc['encoding'],sep='\t',parse_dates=['last_field_trip_date', 'record_created_date', 'record_last_updated_date'])

df_list = [Location(*row) for row in df.itertuples(index=False, name=None)]

# vancouver = City('Vancouver')

# for loc in df_list:
#     vancouver.add_location(loc)

#for i in df_list:
#    print(str(i).split(',')[4],str(i).split(',')[9])

print(df_list[69])
