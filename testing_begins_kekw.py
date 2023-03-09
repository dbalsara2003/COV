import json

from functools import partial

import pyproj
from shapely.geometry import Polygon, Point
import shapely.ops as ops

with open("small_centroidos.json", "r") as f:
    centroids = json.load(f)
    
centroids = centroids["centroids"]

with open("small_coordinatos.json", "r") as f:
    coordinates = json.load(f)
    
coordinates = coordinates["coordinates"]

success_fail = {"success" : 0, "fail" : 0}

for num, centroid in enumerate(centroids):
    print(f"Centroid {num+1} of 1000")
    for coordinate in coordinates:
        if isinstance(coordinate[0][0], list):
            coordinate = coordinate[0]
        polygon = Polygon(coordinate)
        center = Point(centroid[0], centroid[1])
        
        if center.within(polygon):
            success_fail["success"] += 1
            break
    else:
        success_fail["fail"] += 1
        
success_num = success_fail["success"]
fail_num = success_fail["fail"]

print(f"Success: {success_num} Fail: {fail_num}")

print(f"Ratio: {success_num/(success_num+fail_num)}")