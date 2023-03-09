import json

with open("./data/coordinates.json", "r") as f:
    data = json.load(f)

coordinates = data["coordinates"]

print(len(coordinates))

new_list = []

for i, coord in enumerate(coordinates):
    new_list.append(coord)
    
    if len(new_list) == 1000:
        coordinates = {"coordinates" : new_list}
        
        with open(f"./json/coordinates{i-998}_to_{i+1}.json", "w") as f:
            json.dump(coordinates, f, indent=4)
        
        new_list = []

coordinates = {"coordinates" : new_list}

with open(f"./json/coordinates_LAST.json", "w") as f:
    json.dump(coordinates, f, indent=4)