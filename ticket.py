from datetime import datetime
from event import Event
from location import Location
from visitor import VisitorCategory

class Ticket:
    def __init__(self, date: datetime, price: float, event: Event, location: Location, category: VisitorCategory):
        self.date = date
        self.price = price
        self.event = event
        self.location = location
        self.category = category
    # Getter and Setter methods...
