from enum import Enum

class LocationType(Enum):
    PermanentGallery = 1
    ExhibitionHall = 2
    OutdoorSpace = 3

class Location:
    def __init__(self, name: str, location_type: LocationType):
        self.name = name
        self.location_type = location_type
    # Getter and Setter methods...
