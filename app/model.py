# class City:
#     def __init__(self, name, locations=[]):
#         self.name = name
#         self.locations = locations

#     def add_location(self, location):
#         self.locations.append(location)
    
#     def get_location_by_id(self, id):
#         return self.locations[id]
    
#     def get_locations_by_floor_space(self, floor_space):
#         return [location for location in self.locations.values() if location.floor_area_sf >= floor_space]
        
#     def get_locations_by_floor_space_range(self, min_floor_space, max_floor_space):
#         return [location for location in self.locations.values() if location.floor_area_sf >= min_floor_space and location.floor_area_sf <= max_floor_space]

class Location:
    def __init__(self,oid, location_id, area, address, unit, civic_number, street, address_above_door, business_name, floor_area_sf, last_field_trip_date, record_created_date, record_last_updated_date):
        self.oid = oid
        self.location_id = location_id
        self.area = area
        self.address = address
        self.unit = unit
        self.civic_number = civic_number
        self.street = street
        self.address_above_door = address_above_door
        self.business_name = business_name
        self.floor_area_sf = floor_area_sf
        self.last_field_trip_date = last_field_trip_date
        self.record_created_date = record_created_date
        self.record_last_updated_date = record_last_updated_date
    
    def __repr__(self):
        return f'Location: ,{self.location_id},{self.area},{self.address},{self.unit},{self.civic_number},{self.street},{self.address_above_door},{self.business_name},{self.floor_area_sf},{self.last_field_trip_date},{self.record_created_date},{self.record_last_updated_date}'

    def get_by_name(self, name):
        return self.business_name == name
    
class Store:
    def __init__(self, datasetid, recordid, coordinates, unit, geo_point_2d, year_recorded, id, street_name_parcel, retail_category, civic_number_parcel, business_name, geo_local_area, type, record_timestamp):
        self.datasetid = datasetid
        self.recordid = recordid
        self.coordinates = coordinates
        self.unit = unit
        self.geo_point_2d = geo_point_2d
        self.year_recorded = year_recorded
        self.id = id
        self.street_name_parcel = street_name_parcel
        self.retail_category = retail_category
        self.civic_number_parcel = civic_number_parcel
        self.business_name = business_name
        self.geo_local_area = geo_local_area
        self.type = type
        self.record_timestamp = record_timestamp

    def basic_info(self):
        return f"Business name: {self.business_name}, Retail category: {self.retail_category}, located at {self.civic_number_parcel} {self.street_name_parcel} in {self.geo_local_area}"

    def __str__(self) -> str:   
        return f"DataSet ID: {self.datasetid}, RecordID: {self.recordid}, Coordinates: {self.coordinates} Business name: {self.business_name}, Retail category: {self.retail_category}, located at {self.civic_number_parcel} {self.street_name_parcel} in {self.geo_local_area}"

    def __repr__(self) -> str:
        return f"{self.datasetid}, {self.recordid}, {self.coordinates}, {self.unit}, {self.geo_point_2d}, {self.year_recorded}, {self.id}, {self.street_name_parcel}, {self.retail_category}, {self.civic_number_parcel}, {self.business_name}, {self.geo_local_area}, {self.type}, {self.record_timestamp}"

class Stores_list:
    def __init__(self,stores=[]):
        self.stores = stores

    def add_store(self,store):
        self.stores.append(store)

    def get_by_name(self, name):
        stores = [store for store in self.stores if store.business_name == name or name in store.business_name]
        return stores

    def get_by_category(self, category):
        stores = [store for store in self.stores if store.retail_category == category or category in store.retail_category]
        return stores

    def get_by_area(self, area):
        stores = [store for store in self.stores if store.geo_local_area == area or area in store.geo_local_area]
        return stores

    def get_by_civic_number(self, civic_number):
        stores = [store for store in self.stores if store.civic_number_parcel == civic_number]
        return stores

    def __repr__(self) -> str:
        return f"{self.stores}"

    def __str__(self):
        return f"A List of stores with {len(self.stores)} entries"