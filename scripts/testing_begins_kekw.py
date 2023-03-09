import json

import functools

import pyproj
from shapely.geometry import Polygon, Point
import shapely.ops as ops

with open("./data/centroids.json", "r") as f:
    centroids = json.load(f)
    
centroids = centroids["centroids"]

centroids = tuple(centroids)

centroids = tuple(tuple(centroid) for centroid in centroids)

with open("./data/small_coordinatos.json", "r") as f:
    coordinates = json.load(f)
    
coordinates = coordinates["coordinates"]

coordinates = tuple(coordinates)

coordinates = tuple(tuple(tuple(coord) for coord in tuple(coordinate)) for coordinate in coordinates)

# coordinates = tuple(tuple(tuple(tuple(coord2) for coord2 in tuple(coord)) for coord in tuple(coordinate)) for coordinate in coordinates)

actual_coords = ()

for coordinate in coordinates:
    if isinstance(coordinate[0][0], list):
        coordinate = tuple(tuple(tuple(coord2) for coord2 in tuple(coord)) for coord in coordinate)
    actual_coords += (coordinate,)

print(f"{len(actual_coords)} coordinates")
print(f"{len(centroids)} centroids")
success_fail = {"success" : 0, "fail" : 0}

@functools.lru_cache(maxsize=None)
def test_centroid(centroid, coordinates):
    for coordinate in coordinates:
        if isinstance(coordinate[0][0], tuple):
            coordinate = tuple(tuple(coord) for coord in coordinate[0])
        polygon = Polygon(coordinate)
        center = Point(centroid[0], centroid[1])
        
        if center.within(polygon):
            return True
    return False

# for num, centroid in enumerate(centroids):
#     print(f"Centroid {num+1} of 1000")
#     for coordinate in coordinates:
#         if isinstance(coordinate[0][0], list):
#             coordinate = coordinate[0]
#         polygon = Polygon(coordinate)
#         center = Point(centroid[0], centroid[1])
        
#         if center.within(polygon):
#             success_fail["success"] += 1
#             break
#     else:
#         success_fail["fail"] += 1

for num, centroid in enumerate(centroids):
    print(f"Centroid {num+1} of 16406")
    if test_centroid(centroid, actual_coords):
        success_fail["success"] += 1
    else:
        success_fail["fail"] += 1
        
success_num = success_fail["success"]
fail_num = success_fail["fail"]

print(f"Success: {success_num} Fail: {fail_num}")

print(f"Ratio: {success_num/(success_num+fail_num)}")