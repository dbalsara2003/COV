# import json

# with open("coordinates.json", "r") as f:
#     data = json.load(f)
    
# print(len(data))

# coords = [item["geom"]["geometry"]["coordinates"][0] for item in data]

# coordinates = {"coordinates" : coords}

# with open("coordinates.json", "w") as f:
#     json.dump(coordinates, f, indent=4)