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
#     for coordinate in coordinates:
#         if isinstance(coordinates[0][0], tuple):
#             coordinates = tuple(tuple(coord) for coord in coordinate[0])
#     polygon = Polygon(coordinates)
#     center = Point(centroid[0], centroid[1])
#  
#     if center.within(polygon):
#         return True
#     return False

# for num, centroid in enumerate(centroids):
#     print(f"Centroid {num+1} of 1000")
#     if test_centroid(centroid, actual_coords):
#         success_fail["success"] += 1
#     else:
#         success_fail["fail"] += 1

# success_num = success_fail["success"]
# fail_num = success_fail["fail"]

# print(f"Success: {success_num} Fail: {fail_num}")

# print(f"Ratio: {success_num/(success_num+fail_num)}")