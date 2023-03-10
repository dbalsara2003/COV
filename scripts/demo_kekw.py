import json
from shapely.geometry import Point, Polygon

from functools import lru_cache

with open("./data/small_centroidos.json") as f:
    centroids = json.load(f)["centroids"]

with open("./data/small_coordinatos.json") as f:
    coordinates = json.load(f)["coordinates"]

centroids = centroids[:500]
    
centroids = tuple(tuple(centroid) for centroid in centroids)

coordinates = tuple(tuple(tuple(coord) for coord in coordinate) for coordinate in coordinates)

actual_coordinates = ()

for coord in coordinates:
    if isinstance(coord[0][0], list):
        coord = tuple(tuple(small) for small in coord[0])
    actual_coordinates += (coord,)

coordinates = actual_coordinates

print(f"Number of centroids: {len(centroids)}")
print(f"Number of coordinates: {len(coordinates)}")

success = 0
failed = 0

matches = []

@lru_cache(maxsize=None)
def check_point(centroid, coordinates):
    point = Point(centroid)
    polygon = Polygon(coordinates)
    
    if polygon.contains(point) and point.within(polygon):
        return True
    return False

for num, centroid in enumerate(centroids):
    print(f"Checking centroid {num + 1} of {len(centroids)}")
    
    for coords in coordinates:
        if check_point(centroid, coords):
            success += 1
            to_append = {
                num: {
                    "centroid": centroid,
                    "coordinates": coords   
                }
            }
            matches.append(to_append)
            break
    else:
        failed += 1
        
print(f"Success: {success}")
print(f"Failed: {failed}")

print(f"Ratio for {len(centroids)} entries against {len(coordinates)} coordinate values: {(success / (success + failed)) * 100}%")

print("Writing matches to output file...")

with open("demo_matches.json", "w") as f:
    json.dump(matches, f, indent=4)
    print("Done!")