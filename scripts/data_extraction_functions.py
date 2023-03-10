#### DISCLAIMERRRRRRRR ####
### THE BELOW FUNCTIONS WERE INITIALLY USED AS SEPARATE CODE BLOCKS
### SOME CHANGES MIGHT HAVE BEEN MADE TO THE BLOCKS BEFORE BEING PACKED IN FUNCTIONS
### IT'S POSSIBLE THAT THE FUNCTIONS DON'T WORK AS INTENDED ANYMORE
### MAIN POINT THO IS THAT THE CODE IS BUNDLED, REUSUABLE AND READABLE
### THE CODE ITSELF SHOULD BE PRETTY STRAIGHTFORWARD

def all_matches_into_json():
    import json
    from shapely.geometry import Polygon, Point

    with open("point_coordinate_matches.json", "r") as f:
        coordinates = json.load(f)

    all = len(coordinates)
    success = 0


    for key, value in coordinates.items():
        centr = value["centroid"]
        coords = value["coordinates"]
        
        point = Point(centr)
        polygon = Polygon(coords)
        
        if polygon.contains(point):
            success += 1
            
    print(f"Success: {success}")
    print(f"Fail: {all - success}")
    print(f"Success rate: {(success / all) * 100}%")

### THE ABOVE CODE SAVED ALL THE MATCHES IN A JSON FILE ###
###########################################################
###########################################################
###########################################################

def check_unmatched_centroids():
    import json
    from shapely.geometry import Polygon, Point

    with open("point_coordinate_matches.json", "r") as f:
        coordinates = json.load(f)

    with open("./data/centroids.json", "r") as f:
        centroids = json.load(f)["centroids"]
        print("Centroids loaded")
        print(f"Centroids: {len(centroids)}")
        
    matched_centroids = []

    for key, value in coordinates.items():
        centr = value["centroid"]
        matched_centroids.append(centr)
        
    print(f"Matched centroids: {len(matched_centroids)}")
        
    new_centroids = {"centroids_left": []}

    for centroid in centroids:
        if centroid not in matched_centroids:
            new_centroids["centroids_left"].append(centroid)
            
        
    print(len(new_centroids["centroids_left"])) 


### THE ABOVE CODE CHECKS HOW MANY CENTROIDS ARE LEFT AFTER UNMATCHED ###
#######################################################################
#######################################################################
#######################################################################
def unique_centroids_and_count_to_json():
    import json

    with open("./data/centroids.json", "r") as f:
        centroids = json.load(f)["centroids"]
        print("Centroids loaded")
        print(f"Centroids: {len(centroids)}")
        
    repeating_centroids = [{i: None} for i in range(1, 3398)]
    print(len(repeating_centroids))

    unique_centroids = []

    for centroid in centroids:
        if centroid not in unique_centroids:
            unique_centroids.append(centroid)
            
    print(len(unique_centroids))

    for num, centroid in enumerate(unique_centroids):
        repeating_centroids[num][num+1] = {
            "centroid": centroid,
            "count": centroids.count(centroid)
        }

    with open("unique_centroids.json", "w") as f:
        json.dump(repeating_centroids, f, indent=4)

### THE ABOVE CODE SAVES ALL THE UNIQUE CENTROIDS AND HOW MANY TIMES THEY ARE REPEATED IN A JSON FILE###
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

def all_centroids_with_polygons_to_json():
    import json
    from functools import lru_cache

    with open("./data/coordinates.json", "r") as f:
        coordinates = json.load(f)["coordinates"]
        print("Coordinates loaded")
        print(f"Coordinates: {len(coordinates)}")

    @lru_cache(maxsize=None)
    def repeating_coord(coord, repeated):
        for coordinate in repeated:
            if coord == coordinate:
                return True
        return False

    repeating_coordinates = []

    index = 0

    for coord in coordinates:
        if not repeating_coord(coord, repeating_coordinates):
            repeating_coordinates.append(coord)
        if index % 1000 == 0:
            print(f"Index: {index}")

    print(len(repeating_coordinates))

    #### AT THIS POINT THE CODE BLOCK BELOW WAS A DIFFERENT CODE BLOCK INITIALLY ####
    #### MIGHT CAUSE ERRORS IF RUN AS IS ####
    
    with open("unique_centroids.json", "r") as f:
        centroids = json.load(f)
        
    with open("point_coordinate_matches.json", "r") as f:
        matches = json.load(f)
        
    print("DATA LOADED")
    print(len(centroids))
    print(len(matches))
    print("STARTING")

    only_centroids = []

    for item in centroids:
        for key, value in item.items():
            only_centroids.append(value["centroid"])

    unique_matched_centroids = []

    for key, value in matches.items():
        if value["centroid"] not in unique_matched_centroids:
            unique_matched_centroids.append(value["centroid"])
            
    matched_centroids_polygons = []

    for key, value in matches.items():
        if value["centroid"] in unique_matched_centroids:
            if value not in matched_centroids_polygons:
                matched_centroids_polygons.append(value)

    for entry in centroids:
        for key, value in entry.items():
            #If the value for the centroid is in the matched_centroids_polygons list
            #Then append the coordinates to the current dictionary of the centroid         
            for match in matched_centroids_polygons:
                if value["centroid"] == match["centroid"]:
                    value["coordinates"] = match["coordinates"]
                    break

    with open("centroids_with_polygons.json", "w") as f:
        json.dump(centroids, f, indent=4)


### THE ABOVE CODE SAVES ALL THE CENTROIDS WITH THEIR COUNT AND POLYGONS IN A JSON FILE ###
########################################################################################
########################################################################################
########################################################################################

def check_if_centroids_are_within_polygons():
    import json
    from shapely.geometry import Polygon, Point

    with open("centroids_with_polygons.json", "r") as f:
        centroids = json.load(f)
        
    all = len(centroids)
    success = 0
    has_coord = 0

    for item in centroids:
        for key, value in item.items():
            
            if "coordinates" not in value:
                continue
            
            has_coord += 1
            centroid = value["centroid"]
            coords = value["coordinates"]
            
            point = Point(centroid)
            polygon = Polygon(coords)
            
            if polygon.contains(point):
                success += 1
                

    print(f"Entries that have coordinates: {has_coord}")
    print(f"Success: {success}")
    print(f"All: {all}")


#### THE ABOVE CODE CONFIRMS ALL CENTROIDS THAT HAVE POLYGONS ARE WITHIN THE POLYGON ####
######################################################################################
######################################################################################
######################################################################################

def centroids_without_polygons_to_json():
    import json
    from shapely.geometry import Polygon, Point

    with open("centroids_with_polygons.json", "r") as f:
        centroids_with_polygons = json.load(f)
        
    print("DATA LOADED")

    no_polygon = []

    for item in centroids_with_polygons:
        for key, value in item.items():
            if "coordinates" not in value:
                no_polygon.append(value["centroid"])

    no_polygon_json = []

    for i in range(1, len(no_polygon)+1):
        to_append = {
            i: {
                "centroid": no_polygon[i-1],
            }
        }
        
        no_polygon_json.append(to_append)

    with open("./data/polygons.json", "r") as f:
        coordinates = json.load(f)["coordinates"]

    actual_coords = []
            
    for coordinate in coordinates:
        if isinstance(coordinate[0][0], list):
            coordinate = list(list(coord) for coord in coordinate[0])
        actual_coords.append(coordinate)
        
    coordinates = actual_coords

    for i, centroid in enumerate(no_polygon):
        point = Point(centroid)
        
        print(f"Index: {i+1} out of {len(no_polygon)}")
        
        for coordinate in coordinates:
            polygon = Polygon(coordinate)
            
            if polygon.contains(point):
                no_polygon_json[i][i+1]["coordinates"] = coordinate
                break

    with open("centroids_without_polygons.json", "w") as f:
        json.dump(no_polygon_json, f, indent=4)

#### THE ABOVE CODE FINDS THE POLYGONS FOR THE CENTROIDS THAT DON'T HAVE POLYGONS ####
##################################################################################
##################################################################################
##################################################################################

def confirm_all_centroids_have_polygons_but_one_missing():
    import json
    from shapely.geometry import Polygon, Point

    with open("centroids_without_polygons.json", "r") as f:
        centroids_without_polygons = json.load(f)
        
    all = len(centroids_without_polygons)

    has_coordinate = 0

    for item in centroids_without_polygons:
        for key, value in item.items():
            if "coordinates" in value:
                has_coordinate += 1
            else:
                print(value)
                
    print(f"Has coordinate: {has_coordinate}")
    print(f"All: {all}")

    with open("./data/polygons.json", "r") as f:
        coordinates = json.load(f)["coordinates"]
        
    actual_coords = []

    for coordinate in coordinates:
        if isinstance(coordinate[0][0], list):
            coordinate = list(list(coord) for coord in coordinate[0])
        actual_coords.append(coordinate)

    point = [-123.09983012512932, 49.27294592860098]

    for coordinate in actual_coords:
        polygon = Polygon(coordinate)
        point = Point(point)
        if polygon.contains(point):
            print("YES")
            break
    else:
        print("NO POLYGON FOR THIS POINT")


### THE ABOVE CODE CONFIRMS ALL THE NEW CENTROIDS HAVE POLYGONS ###
### IT ALSO CONFIRMS THAT THERE IS ONLY ONE CENTROID WITH NO POLYGON ###
#####################################################################
#####################################################################
#####################################################################


def add_polygons_to_centroids_with_polygons():
    import json

    with open("centroids_with_polygons.json", "r") as f:
        centroids_with_polygons = json.load(f)
        
    with open("centroids_without_polygons.json", "r") as f:
        centroids_without_polygons = json.load(f)

    for item in centroids_without_polygons:
        for key, value in item.items():
            
            stop = False
            
            if "coordinates" not in value:
                continue
            
            to_append = {
                "coordinates": value["coordinates"],
            }
            
            for centroid in centroids_with_polygons:
                for key2, value2 in centroid.items():
                    if value["centroid"] == value2["centroid"]:
                        value2.update(to_append)
                        stop = True
                        break
                if stop:
                    break

    has_coords = 0
    original_with_coords = 2604

    for item in centroids_with_polygons:
        for key, value in item.items():
            if "coordinates" in value:
                has_coords += 1

    print(f"Original with coords: {original_with_coords}")
    print(f"New with coords: {has_coords}")

    with open("centroids_with_polygons.json", "w") as f:
        json.dump(centroids_with_polygons, f, indent=4)

### THE ABOVE CODE ADDS THE POLYGONS TO THE CENTROIDS THAT HAD NO POLYGONS ###
###########################################################################
###########################################################################
###########################################################################


def confirm_all_centroids_have_polygons_final_test():
    import json
    from shapely.geometry import Polygon, Point

    with open("centroids_with_polygons.json", "r") as f:
        centroids_with_polygons = json.load(f)
        
    full_success = 0
    target = 3396
        
    for item in centroids_with_polygons:
        for key, value in item.items():
            if "coordinates" not in value:
                continue
            
            point = Point(value["centroid"])
            polygon = Polygon(value["coordinates"])
            
            if point.within(polygon):
                full_success += 0.5
                
            if polygon.contains(point):
                full_success += 0.5
                
    print(f"Success: {full_success}")
    print(f"Target: {target}")

    if full_success == target:
        print("GG LET'S FUCKING GOOOOOO")


### THE ABOVE CODE CONFIRMS THAT ALL THE CENTROIDS HAVE POLYGONS AND ARE WITHIN THEM ###
####################################################################################
####################################################################################
####################################################################################
####################################################################################

def fix_indices_in_centroids_with_polygons():
    import json

    with open("centroids_with_polygons.json", "r") as f:
        centroids_with_polygons = json.load(f)

    fixed_indices = [i for i in range(1, 3397)]
    fixed_indices = fixed_indices[::-1]

    fixed_data = []

    for entry in centroids_with_polygons:
        for key, value in entry.items():
            to_append = {
                fixed_indices.pop(): value
            }
            fixed_data.append(to_append)

    with open("centroids_with_polygons.json", "w") as f:
        json.dump(fixed_data, f, indent=4)

### THE ABOVE CODE JUST FIXED THE INDICES OF THE ENTRIES IN THE CENTROID POLYGON FILE ###
#########################################################################################
#########################################################################################
#########################################################################################


def calculate_area_of_storefronts():
    import json
    from math import ceil

    from functools import partial

    import pyproj
    from shapely.geometry import Polygon
    import shapely.ops as ops


    with open("centroids_with_polygons.json", "r") as f:
        centroids_with_polygons = json.load(f)
    
    #This variable is the ratio that fixes the difference between actual area and area calculated by shapely
    magic_number = 0.00099

    for item in centroids_with_polygons:
        for key, value in item.items():
            
            current_count = value["count"]
            current_coords = value["coordinates"]
            
            total_area_sm = 0
            total_area_sf = 0
            average_area_per_storefront_sf = 0
            
            polygon = Polygon(current_coords)
            
            geom_area = ops.transform(
                partial(
                    pyproj.transform,
                    pyproj.Proj(init='EPSG:4326'),
                    pyproj.Proj(proj="aea",
                                lat_1=polygon.bounds[1],
                                lat_2=polygon.bounds[3])),
                polygon
            )
            
            total_area_sm = ceil(geom_area.area/magic_number)
            total_area_sf = ceil(geom_area.area/magic_number*10.7639104)
            average_area_per_storefront_sf = ceil(total_area_sf/current_count)
            
            #Update the current dictionary by adding the new keys and values
            
            value.update({
                "total_area_sm": total_area_sm,
                "total_area_sf": total_area_sf,
                "average_area_per_storefront_sf": average_area_per_storefront_sf
            })

    #Write the changes to the file

    with open("centroids_with_polygons.json", "w") as f:
        json.dump(centroids_with_polygons, f, indent=4)
        
### THE ABOVE CODE CALCULATES THE AREA OF EACH POLYGON AND THE AVERAGE AREA PER STOREFRONT ###
#############################################################################################

                        ###### DISCLAIMER ######
                     
### THIS CODE RUNS FINE BUT YOUR TERMINAL WILL BE SPAMMED WITH WARNINGS ###
### THIS IS BECAUSE SOME OF THE FUNCTIONS IN USE ARE DEPRECATED ###
### DON'T WORRY ABOUT IT, THE FUNCTION SHOULD ALWAYS BE RNNING FINE AND GIVING THE SAME OUTPUT ###

                     ###### END OF DISCLAIMER ######
                     
#############################################################################################
#############################################################################################
#############################################################################################

