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
        return f'Location {self.oid},{self.location_id},{self.area},{self.address},{self.unit},{self.civic_number},{self.street},{self.address_above_door},{self.business_name},{self.floor_area_sf},{self.last_field_trip_date},{self.record_created_date},{self.record_last_updated_date}'

    def get_by_name(self, name):
        return self.business_name == name
