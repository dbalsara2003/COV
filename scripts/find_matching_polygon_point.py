import json

import functools

import pyproj
from shapely.geometry import Polygon, Point
import shapely.ops as ops

with open("./data/points.json", "r") as f:
    centroids = json.load(f)
    
centroids = centroids["centroids"]

centroids = tuple(centroids)

centroids = tuple(tuple(centroid) for centroid in centroids)

with open("./data/polygons.json", "r") as f:
    coordinates = json.load(f)
    
coordinates = coordinates["coordinates"]

coordinates = tuple(coordinates)

coordinates = tuple(tuple(tuple(coord) for coord in tuple(coordinate)) for coordinate in coordinates)

# coordinates = tuple(tuple(tuple(tuple(coord2) for coord2 in tuple(coord)) for coord in tuple(coordinate)) for coordinate in coordinates)

actual_coords = ()
total = len(coordinates)
for count, coordinate in enumerate(coordinates):
    # Get percentage from count
    print(f"Converted {str((count/total)*100)[0:5]}% to hashable data.")
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
            return (True, coordinate)
    return (False, 0)

with open("poly_point.csv", mode="a+") as file:
    file.write("point;polygon\n")
    for num, centroid in enumerate(centroids):
        print(f"Centroid {num+1} of 16406")
        return_tuple = test_centroid(centroid, actual_coords)
        if return_tuple[0]:
            file.write(f"{centroid};{return_tuple[1]}\n")
            success_fail["success"] += 1
        else:
            success_fail["fail"] += 1
            
success_num = success_fail["success"]
fail_num = success_fail["fail"]

print(f"Success: {success_num} Fail: {fail_num}")
print(f"Ratio: {success_num/(success_num+fail_num)}")