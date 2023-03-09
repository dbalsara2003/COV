import json

with open('tamim.json', 'r') as f:
    data = json.load(f)

    print(data['records'][0])