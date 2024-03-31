from datetime import datetime
from location import Location

class Event:
    def __init__(self, name: str, start_time: datetime, end_time: datetime, location: Location):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
    # Getter and Setter methods...

class Exhibition(Event):
    def __init__(self, name: str, start_time: datetime, end_time: datetime, location: Location, curator_name: str):
        super().__init__(name, start_time, end_time, location)
        self.curator_name = curator_name
    # Getter and Setter methods...


class Tour(Event):
    def __init__(self, name: str, start_time: datetime, end_time: datetime, location: Location, guide_name: str, visitor_limit: int, description: str):
        super().__init__(name, start_time, end_time, location)
        self.guide_name = guide_name
        self.visitor_limit = visitor_limit
        self.description = description
    # Getter and Setter methods...


class SpecialEvent(Event):
    def __init__(self, name: str, start_time: datetime, end_time: datetime, location: Location, sponsors: str, purpose: str, price: float):
        super().__init__(name, start_time, end_time, location)
        self.sponsors = sponsors
        self.purpose = purpose
        self.price = price
    # Getter and Setter methods...
