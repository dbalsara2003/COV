# import json

# with open("centroids.json", "r") as f:
#     data = json.load(f)

# print(len(data))

# cents = [item["geom"]["geometry"]["coordinates"] for item in data]

# centroids = {"centroids" : cents}

# with open("centroids.json", "w") as f:
#     json.dump(centroids, f, indent=4)