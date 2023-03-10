##### ATTEMPT 1 #####
####################
####################
####################

# import json
# import os
# from functools import lru_cache
# from shapely.geometry import Polygon, Point

# # Load centroids from JSON file
# with open("./data/centroids.json", "r") as f:
#     centroids = json.load(f)["centroids"]

# # Convert centroids to tuples of tuples
# centroids = tuple(map(tuple, centroids))

# # Get a list of all JSON files in the directory
# json_files = [filename for filename in os.listdir("./json/") if filename.endswith(".json")]

# # Set up a cache for the test_centroid function
# @lru_cache(maxsize=None)
# def test_centroid(min_x, max_x, min_y, max_y, centroid):
#     return min_x <= centroid[0] <= max_x and min_y <= centroid[1] <= max_y

# # Define a function to check if a centroid is inside a polygon
# def is_centroid_inside_polygon(centroid, polygon):
#     min_x, min_y = map(min, zip(*polygon))
#     max_x, max_y = map(max, zip(*polygon))
#     return test_centroid(min_x, max_x, min_y, max_y, centroid)

# # Iterate over all JSON files and check if each centroid is inside any of the polygons
# success_count = 0
# failure_count = 0
# for i, json_file in enumerate(json_files):
#     print(f"Processing file {i+1} of {len(json_files)}: {json_file}")
    
#     # Load the polygon coordinates from the JSON file
#     with open(f"./json/{json_file}", "r") as f:
#         coordinates = json.load(f)["coordinates"]
    
#     # Convert coordinates to tuples of tuples
#     polygons = [tuple(map(tuple, polygon[0])) for polygon in coordinates if isinstance(polygon[0][0], list)]
    
#     # Check each centroid against each polygon
#     for centroid in centroids:
#         for polygon in polygons:
#             if is_centroid_inside_polygon(centroid, polygon):
#                 success_count += 1
#                 break
#         else:
#             failure_count += 1
    
#     # Clear the cache every 5 files to prevent it from using up too much memory
#     if (i+1) % 5 == 0:
#         test_centroid.cache_clear()

# print(f"Centroids inside polygons: {success_count}")
# print(f"Centroids outside polygons: {failure_count}")
# print(f"Success ratio: {success_count / (success_count + failure_count)}")

##### END OF ATTEMPT 1 #####
############################
############################
############################




##### ATTEMPT 2 #####
####################
####################
####################

# import json
# from shapely.geometry import Polygon, Point
# import os

# # Load centroids from JSON file
# with open("./data/centroids.json", "r") as f:
#     centroids = json.load(f)["centroids"]

# points = [Point(centroid) for centroid in centroids]

# # Load polygons from JSON files
# json_files = os.listdir("./json/")
# # polygons = []
# # for file in json_files:
#     # with open(f"./json/{file}", "r") as f:
#         # data = json.load(f)["coordinates"]
#         # polygons.extend(Polygon(coords[0]) for coords in data)
#         # coordinates = json.load(f)["coordinates"]
#         # polygons = [tuple(map(tuple, polygon[0])) for polygon in coordinates if isinstance(polygon[0][0], list)]
#         # for coords in data:
#         #     if len(coords) == 3:
#         #         print(coords)
#         #         coords = coords[0]
#         #         print(coords)
#         #     polygons.append(Polygon(coords))

# # Iterate through centroids and check if they are contained within any polygons
# success_count = 0
# i = 1
# last = 101
# for file in json_files:
#     print("Processing file", i, "of", last)
#     i += 1
#     with open(f"./json/{file}", "r") as f:
#         # data = json.load(f)["coordinates"]
#         # polygons.extend(Polygon(coords[0]) for coords in data)
#         coordinates = json.load(f)["coordinates"]
    
#     polygons = [tuple(map(tuple, polygon[0])) for polygon in coordinates if isinstance(polygon[0][0], list)]
        
#     for point in points:
#         for polygon in polygons:
#             polygon = Polygon(polygon)
#             if point.within(polygon):
#                 success_count += 1
#                 break

# # Calculate success and failure rates
# total_count = len(centroids)
# failure_count = total_count - success_count
# success_rate = success_count / total_count

# print(f"Success: {success_count} Fail: {failure_count}")
# print(f"Ratio: {success_rate}")


###### END OF ATTEMPT 2 #####
#############################
#############################
#############################



##### ATTEMPT 3 #####
####################
####################
####################

# import json
# import time
# import pygeos
# import os

# def load_polygons():
#     polygons = []
#     for filename in os.listdir('./json'):
#         with open(f'./json/{filename}') as f:
#             data = json.load(f)["coordinates"]
#             for coords in data:
#                 if isinstance(coords[0][0], list):
#                     coords = tuple(coords[0])
#                 pol = Geometry("POLYGON " + str(tuple(coords[0])))
#                 polygons.append(pol)
#     return pygeos.geometry.join(polygons)

# def load_centroids():
    # with open('./data/centroids.json') as f:
        # data = json.load(f)["centroids"]
    # return pygeos.points_from_xy([x[0] for x in data['centroids']], [x[1] for x in data['centroids']])

# def find_centroids_in_polygons(centroids, polygons):
    # return pygeos.boolean_contains(polygons, centroids)

# start_time = time.time()

# polygons = load_polygons()
# centroids = load_centroids()

# contained = find_centroids_in_polygons(centroids, polygons)
# success_num = pygeos.count_true(contained)
# fail_num = len(centroids) - success_num

# print(f"Success: {success_num} Fail: {fail_num}")
# print(f"Ratio: {success_num / len(centroids)}")
# print(f"Elapsed time: {time.time() - start_time:.2f}s")


##### END OF ATTEMPT 3 #####
############################
############################
############################



##### ATTEMPT 4 #####
####################
####################
####################

# import json
# import time
# import pygeos
# import os

# with open("./data/centroids.json", "r") as f:
#     centroids = json.load(f)["centroids"]
#     centroids = pygeos.coordinates.from_xy(centroids[:, 0], centroids[:, 1])

# workdir = os.getcwd()
# json_files = os.listdir(workdir + "/json/")
    
# success_fail = {"success" : 0, "fail" : 0}

# for i, file in enumerate(json_files, 1):
#     print(f"Using file {i} of {len(json_files)}")
    
#     with open(f"./json/{file}", "r") as f:
#         data = json.load(f)
        
#         coordinates = pygeos.coordinates.from_xy(data["coordinates"][0][:, 0], data["coordinates"][0][:, 1])
#         polygon = pygeos.creation.polygon(coordinates)

#     centroids_in_polygon = pygeos.boolean.contains(polygon, centroids)
#     num_successes = centroids_in_polygon.sum()
#     success_fail["success"] += num_successes
#     success_fail["fail"] += len(centroids) - num_successes
    
#     print(f"Success: {num_successes} Fail: {len(centroids) - num_successes}")
    
#     pygeos.clear_cache()

# success_num = success_fail["success"]
# fail_num = success_fail["fail"]

# print(f"Success: {success_num} Fail: {fail_num}")
# print(f"Ratio: {success_num/(success_num+fail_num)}")


#### END OF ATTEMPT 4 #####
###########################
###########################
###########################