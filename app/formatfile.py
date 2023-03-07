##I don't really know how we want the data to be parsed so if someone could work on this with me would be very helpful :P
import pandas as pd
import chardet
from model import *

def csvParse(file):
    uf = f'uploaded_files/{file.filename}'
    with open(uf, 'rb') as f:
        enc = chardet.detect(f.read())
    
    df = pd.read_csv(uf, encoding = enc['encoding'], sep='\t', parse_dates=['last_field_trip_date', 'record_created_date', 'record_last_updated_date'])
        
    return df