import json
import time
import functools

import pyproj
from shapely.geometry import Polygon, Point
import shapely.ops as ops

import os

with open("./data/centroids.json", "r") as f:
    centroids = json.load(f)
    
centroids = centroids["centroids"]

centroids = tuple(centroids)

centroids = tuple(tuple(centroid) for centroid in centroids)

# with open("./data/small_coordinatos.json", "r") as f:
#     coordinates = json.load(f)
    
# coordinates = coordinates["coordinates"]

# coordinates = tuple(coordinates)

# coordinates = tuple(tuple(tuple(coord) for coord in tuple(coordinate)) for coordinate in coordinates)

# coordinates = tuple(tuple(tuple(tuple(coord2) for coord2 in tuple(coord)) for coord in tuple(coordinate)) for coordinate in coordinates)

# ##WEIRD TESTING OF COORDINATES###
# ##################################################################################
# ##################################################################################
# ##################################################################################

# actual_coords = ()

# for coordinate in coordinates:
#     if isinstance(coordinate[0][0], list):
#         coordinate = tuple(tuple(tuple(coord2) for coord2 in tuple(coord)) for coord in coordinate)
#     actual_coords += (coordinate,)

# print(f"{len(actual_coords)} coordinates")
# print(f"{len(centroids)} centroids")
# success_fail = {"success" : 0, "fail" : 0}

# @functools.lru_cache(maxsize=None)
# def test_centroid(centroid, coordinates):
#     if isinstance(coordinates[0][0], tuple):
#         coordinates = tuple(tuple(coord) for coord in coordinates[0])
#     polygon = Polygon(coordinates)
#     center = Point(centroid[0], centroid[1])
        
#     if center.within(polygon):
#         return True
#     return False

# # for num, centroid in enumerate(centroids):
# #     print(f"Centroid {num+1} of 1000")
# #     for coordinate in coordinates:
# #         if isinstance(coordinate[0][0], list):
# #             coordinate = coordinate[0]
# #         polygon = Polygon(coordinate)
# #         center = Point(centroid[0], centroid[1])
        
# #         if center.within(polygon):
# #             success_fail["success"] += 1
# #             break
# #     else:
# #         success_fail["fail"] += 1

# num_centroid = 1

# actual_coords = list(actual_coords)
# centroids = list(centroids)

# for i, coordinate in enumerate(actual_coords):
#     for num, centroid in enumerate(centroids):
#         if test_centroid(centroid, coordinate):
#             success_fail["success"] += 1
#             print(f"Centroid {num_centroid} of 16406 PASSED THE TEST")
#             num_centroid += 1
#             centroids.pop(num)
#             break
#     else:
#         print(f"Centroid {num_centroid} of 16406 ....................")
#         num_centroid += 1
#         success_fail["fail"] += 1

# # for num, centroid in enumerate(centroids):
# #     print(f"Centroid {num+1} of 16406")
# #     if test_centroid(centroid, actual_coords):
# #         success_fail["success"] += 1
# #     else:
# #         success_fail["fail"] += 1
        
# success_num = success_fail["success"]
# fail_num = success_fail["fail"]

# print(f"Success: {success_num} Fail: {fail_num}")

# print(f"Ratio: {success_num/(success_num+fail_num)}")

# #####END OF WEIRD TESTING OF COORDINATES###
# ##################################################################################
# ##################################################################################
# ##################################################################################


# ###### ORIGINAL CODE #######
# ##################################################################################
# ##################################################################################

# actual_coords = ()

# for coordinate in coordinates:
#     if isinstance(coordinate[0][0], list):
#         coordinate = tuple(tuple(tuple(coord2) for coord2 in tuple(coord)) for coord in coordinate)
#     actual_coords += (coordinate,)

# print(f"{len(actual_coords)} coordinates")
# print(f"{len(centroids)} centroids")
# success_fail = {"success" : 0, "fail" : 0}

# @functools.lru_cache(maxsize=None)
# def test_centroid(centroid):
#     global actual_coords
#     actual_coords = list(actual_coords)
#     for num, coordinate in enumerate(actual_coords):
#         if isinstance(coordinate[0][0], tuple):
#             coordinate = tuple(tuple(coord) for coord in coordinate[0])
            
#         polygon = Polygon(coordinate)
#         center = Point(centroid[0], centroid[1])

#         if center.within(polygon):
#             actual_coords.pop(num)
#             return True
#     return False

# for num, centroid in enumerate(centroids):
#     print(f"Centroid {num+1} of 16406")
#     if test_centroid(centroid):
#         success_fail["success"] += 1
#     else:
#         success_fail["fail"] += 1

# success_num = success_fail["success"]
# fail_num = success_fail["fail"]

# print(f"Success: {success_num} Fail: {fail_num}")

# print(f"Ratio: {success_num/(success_num+fail_num)}")

# ######## END OF ORIGINAL CODE #########
# ################################################################################## 
# ##################################################################################
# ##################################################################################






# ###EH RANDOM TESTING OF COORDINATES###
# ##################################################################################
# ##################################################################################
# ##################################################################################


# actual_coords = ()

# for coordinate in coordinates:
#     if isinstance(coordinate[0][0], list):
#         coordinate = tuple(tuple(tuple(coord2) for coord2 in tuple(coord)) for coord in coordinate)
#     actual_coords += (coordinate,)

# print(f"{len(actual_coords)} coordinates")
# print(f"{len(centroids)} centroids")
# success_fail = {"success" : 0, "fail" : 0}

# @functools.lru_cache(maxsize=None)
# def test_centroid(centroid, coordinates):
#     if isinstance(coordinates[0][0], list):
#         coordinates = tuple(tuple(coord) for coord in coordinate[0])
#     print(coordinates)
#     polygon = Polygon(coordinates)
#     center = Point(centroid[0], centroid[1])
        
#     if center.within(polygon):
#         return True
#     return False

# # for num, centroid in enumerate(centroids):
# #     print(f"Centroid {num+1} of 1000")
# #     for coordinate in coordinates:
# #         if isinstance(coordinate[0][0], list):
# #             coordinate = coordinate[0]
# #         polygon = Polygon(coordinate)
# #         center = Point(centroid[0], centroid[1])
        
# #         if center.within(polygon):
# #             success_fail["success"] += 1
# #             break
# #     else:
# #         success_fail["fail"] += 1

# for num, centroid in enumerate(centroids):
#     print(f"Centroid {num+1} of 16406")
#     for coordinates in actual_coords:
#         if test_centroid(centroid, actual_coords):
#             success_fail["success"] += 1
#             break
#     else:
#         success_fail["fail"] += 1
        
# success_num = success_fail["success"]
# fail_num = success_fail["fail"]

# print(f"Success: {success_num} Fail: {fail_num}")

# print(f"Ratio: {success_num/(success_num+fail_num)}")

# ###END OF RANDOM TESTING OF COORDINATES###
# ##################################################################################
# ##################################################################################
# ##################################################################################




# ##### TESTING OF COORDINATES USING SMALL JSON FILES###
# ##################################################################################
# ##################################################################################
# ##################################################################################

# workdir = os.getcwd()
# json_files = os.listdir(workdir + "/json/")

# num_centroid = 1

# success_fail = {"success" : 0, "fail" : 0}

# @functools.lru_cache(maxsize=None)
# def test_centroid(centroid, coordinates):
#     for coordinate in coordinates:
#         if isinstance(coordinate[0][0], tuple):
#             coordinate = tuple(tuple(coord) for coord in coordinates[0])
            
#         polygon = Polygon(coordinate)
#         center = Point(centroid[0], centroid[1])
#         if center.within(polygon):
#             return True
        
#     return False

# centroids = list(centroids)

# for file in json_files:
#     with open(f"./json/{file}", "r") as f:
#         data = json.load(f)
        
#         print(len(centroids))
        
#         coordinates = data["coordinates"]
        
#         coordinates = tuple(coordinates)

#         coordinates = tuple(tuple(tuple(coord) for coord in tuple(coordinate)) for coordinate in coordinates)
        
#         actual_coords = ()

#         for coordinate in coordinates:
#             if isinstance(coordinate[0][0], list):
#                 coordinate = tuple(tuple(tuple(coord2) for coord2 in tuple(coord)) for coord in coordinate)
#             actual_coords += (coordinate,)
        
#         for num, centroid in enumerate(centroids):
#             if test_centroid(centroid, actual_coords):
#                 print(f"Centroid {num_centroid} of 16406")
#                 num_centroid += 1
#                 success_fail["success"] += 1
#                 centroids.pop(num)
#             else:
#                 success_fail["fail"] += 1

# #### END OF TESTING OF COORDINATES USING SMALL JSON FILES###
# ##################################################################################
# ##################################################################################




# #### TESTING A NEW COORDINATE FUNCTION###
# ##################################################################################
# ##################################################################################
# ##################################################################################

# workdir = os.getcwd()
# json_files = os.listdir(workdir + "/json/")

# actual_coords = ()

# for coordinate in coordinates:
#     if isinstance(coordinate[0][0], list):
#         coordinate = tuple(tuple(coord) for coord in coordinate[0])
#     actual_coords += (coordinate,)
    
# success_rate = 0

# point_coordinates = {}

# @functools.lru_cache(maxsize=None)
# def test_centroid(min_x, max_x, min_y, max_y, centroid):
#     if (min_x <= centroid[0] <= max_x) and (min_y <= centroid[1] <= max_y):
#         return True
#     return False

# centroids = list(centroids)

# def testing(centroids, coordinates):
#     global success_rate
    
#     for num, centroid in enumerate(centroids):
#         for coordinate in coordinates:
#             min_x = min(coordinate, key=lambda x: x[0])[0]
#             max_x = max(coordinate, key=lambda x: x[0])[0]
#             min_y = min(coordinate, key=lambda y: y[1])[1]
#             max_y = max(coordinate, key=lambda y: y[1])[1]
            
#             if test_centroid(min_x, max_x, min_y, max_y, centroid):
#                 centroids.pop(num)
#                 point_coordinates[num] = {
#                     "centroid" : centroid,
#                     "coordinates" : coordinate
#                 }
#                 success_rate += 1
#                 break
            

# def open_json(file):
#     with open(f"./json/{file}", "r") as f:
#         data = json.load(f)
        
#         coordinates = data["coordinates"]
        
#         coordinates = tuple(coordinates)

#         coordinates = tuple(tuple(tuple(coord) for coord in tuple(coordinate)) for coordinate in coordinates)
        
#         actual_coords = ()
        
#         for coordinate in coordinates:
#             if isinstance(coordinate[0][0], list):
#                 coordinate = tuple(tuple(coord) for coord in coordinate[0])
#             actual_coords += (coordinate,)
    
#     return actual_coords

# i = 1

# for file in json_files:
    
#     print(len(point_coordinates))
#     print(f"\nTotal centroids left: {len(centroids)}\n")
    
#     actual_coords = open_json(file)
    
#     print(f"Using file {i} of 100")

#     testing(centroids, actual_coords)
    
#     if i % 10 == 0:
#         test_centroid.cache_clear()
    
#     i += 1

# with open("point_coordinates.json", "w") as f:
#     json.dump(point_coordinates, f, indent=4)

# print(f"Success: {success_rate}")

# print(f"Ratio: {success_rate/16406}")


# ---------------- ABOVE IS THE INITIAL SOLUTION ----------------


# ---------------- BELOW IS THE OPTIMIZED SOLUTION ----------------

workdir = os.getcwd()
json_files = os.listdir(workdir + "/json/")
    
success_rate = 0

point_coordinates = {}

@functools.lru_cache(maxsize=None)
def test_centroid(centroid, coordinates):
    point = Point(centroid[0], centroid[1])
    polygon = Polygon(coordinates)
    if point.within(polygon):
        return True
    return False

centroids = list(centroids)

def testing(centroids, coordinates):
    global success_rate
    
    for num, centroid in enumerate(centroids):
        for coordinate in coordinates:
            min_x = min(coordinate, key=lambda x: x[0])[0]
            max_x = max(coordinate, key=lambda x: x[0])[0]
            min_y = min(coordinate, key=lambda y: y[1])[1]
            max_y = max(coordinate, key=lambda y: y[1])[1]
            
            if test_centroid(min_x, max_x, min_y, max_y, centroid):
                centroids.pop(num)
                point_coordinates[num] = {
                    "centroid" : centroid,
                    "coordinates" : coordinate
                }
                success_rate += 1
                break
            

def open_json(file):
    with open(f"./json/{file}", "r") as f:
        data = json.load(f)
        
        coordinates = data["coordinates"]
        
        coordinates = tuple(coordinates)

        coordinates = tuple(tuple(tuple(coord) for coord in tuple(coordinate)) for coordinate in coordinates)
        
        actual_coords = ()
        
        for coordinate in coordinates:
            if isinstance(coordinate[0][0], list):
                coordinate = tuple(tuple(coord) for coord in coordinate[0])
            actual_coords += (coordinate,)
    
    return actual_coords

i = 1

for file in json_files:
    
    print(len(point_coordinates))
    print(f"\nTotal centroids left: {len(centroids)}\n")
    
    actual_coords = open_json(file)
    
    print(f"Using file {i} of 100")

    testing(centroids, actual_coords)
    
    if i % 10 == 0:
        test_centroid.cache_clear()
    
    i += 1

with open("point_coordinates.json", "w") as f:
    json.dump(point_coordinates, f, indent=4)

print(f"Success: {success_rate}")

print(f"Ratio: {success_rate/16406}")