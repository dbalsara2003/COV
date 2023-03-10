

import pandas, numpy, json



with open('./poly_point.csv', mode='r') as f:
    lines = f.readlines()

for count, line in enumerate(lines):
    lines[count] = lines[count].replace('\n','')