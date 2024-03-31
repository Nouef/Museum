from datetime import datetime
from location import Location

class Artwork:
    def __init__(self, title: str, artist: str, date_of_creation: datetime, historical_significance: str, location: Location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location
    # Getter and Setter methods...
