from datetime import datetime
from enum import Enum
from typing import List, Union

class LocationType(Enum):
    PermanentGallery = 1
    ExhibitionHall = 2
    OutdoorSpace = 3

class VisitorCategory(Enum):
    Adult = 1
    Child = 2
    Teacher = 3
    Student = 4
    Senior = 5
    Group = 6

class Location:
    def __init__(self, name: str, type: LocationType):
        self.__name = name
        self.__type = type

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_type(self) -> LocationType:
        return self.__type

    def set_type(self, type: LocationType) -> None:
        self.__type = type

class Artwork:
    def __init__(self, title: str, artist: str, dateOfCreation: datetime, historicalSignificance: str, location: Location):
        self.__title = title
        self.__artist = artist
        self.__dateOfCreation = dateOfCreation
        self.__historicalSignificance = historicalSignificance
        self.__location = location

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str) -> None:
        self.__title = title

    def get_artist(self) -> str:
        return self.__artist

    def set_artist(self, artist: str) -> None:
        self.__artist = artist

    def get_dateOfCreation(self) -> datetime:
        return self.__dateOfCreation

    def set_dateOfCreation(self, dateOfCreation: datetime) -> None:
        self.__dateOfCreation = dateOfCreation

    def get_historicalSignificance(self) -> str:
        return self.__historicalSignificance

    def set_historicalSignificance(self, historicalSignificance: str) -> None:
        self.__historicalSignificance = historicalSignificance

    def get_location(self) -> Location:
        return self.__location

    def set_location(self, location: Location) -> None:
        self.__location = location

class Ticket:
    def __init__(self, date: datetime, price: float, eventName: str, location: Location, category: VisitorCategory):
        self.__date = date
        self.__price = price
        self.__eventName = eventName
        self.__location = location
        self.__category = category

    def get_date(self) -> datetime:
        return self.__date

    def set_date(self, date: datetime) -> None:
        self.__date = date

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price: float) -> None:
        self.__price = price

    def get_eventName(self) -> str:
        return self.__eventName

    def set_eventName(self, eventName: str) -> None:
        self.__eventName = eventName

    def get_location(self) -> Location:
        return self.__location

    def set_location(self, location: Location) -> None:
        self.__location = location

    def get_category(self) -> VisitorCategory:
        return self.__category

    def set_category(self, category: VisitorCategory) -> None:
        self.__category = category

class Visitor:
    def __init__(self, name: str, email: str, age: int, category: VisitorCategory):
        self.__name = name
        self.__email = email
        self.__age = age
        self.__category = category
        self.__tickets = []

    def purchase_ticket(self, event, pricing_strategy, base_price):
        price = pricing_strategy.calculate_price(base_price, self.__category, self.__age)
        ticket = Ticket(datetime.now(), price, event.get_name(), event.get_location(), self.__category)
        self.__tickets.append(ticket)
        return ticket

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str) -> None:
        self.__email = email

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        self.__age = age

    def get_category(self) -> VisitorCategory:
        return self.__category

    def set_category(self, category: VisitorCategory) -> None:
        self.__category = category

    def get_tickets(self) -> List[Ticket]:
        return self.__tickets

    def add_ticket(self, ticket: Ticket) -> None:
        self.__tickets.append(ticket)

class Event:
    def __init__(self, name: str, startTime: datetime, endTime: datetime, location: Location):
        self.__name = name
        self.__startTime = startTime
        self.__endTime = endTime
        self.__location = location

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_startTime(self) -> datetime:
        return self.__startTime

    def set_startTime(self, startTime: datetime) -> None:
        self.__startTime = startTime

    def get_endTime(self) -> datetime:
        return self.__endTime

    def set_endTime(self, endTime: datetime) -> None:
        self.__endTime = endTime

    def get_location(self) -> Location:
        return self.__location

    def set_location(self, location: Location) -> None:
        self.__location = location

class Exhibition(Event):
    def __init__(self, name: str, startTime: datetime, endTime: datetime, location: Location, curatorName: str):
        super().__init__(name, startTime, endTime, location)
        self.__curatorName = curatorName

    def get_curatorName(self) -> str:
        return self.__curatorName

    def set_curatorName(self, curatorName: str) -> None:
        self.__curatorName = curatorName


class Tour(Event):
    def __init__(self, name: str, startTime: datetime, endTime: datetime, location: Location, guideName: str, visitorLimit: int):
        super().__init__(name, startTime, endTime, location)
        self.__guideName = guideName
        self.__visitorLimit = visitorLimit

    def get_guideName(self) -> str:
        return self.__guideName

    def set_guideName(self, guideName: str) -> None:
        self.__guideName = guideName

    def get_visitorLimit(self) -> int:
        return self.__visitorLimit

    def set_visitorLimit(self, visitorLimit: int) -> None:
        self.__visitorLimit = visitorLimit


class SpecialEvent(Event):
    def __init__(self, name: str, startTime: datetime, endTime: datetime, location: Location, sponsors: str, purpose: str, price: float):
        super().__init__(name, startTime, endTime, location)
        self.__sponsors = sponsors
        self.__purpose = purpose
        self.__price = price

    def get_sponsors(self) -> str:
        return self.__sponsors

    def set_sponsors(self, sponsors: str) -> None:
        self.__sponsors = sponsors

    def get_purpose(self) -> str:
        return self.__purpose

    def set_purpose(self, purpose: str) -> None:
        self.__purpose = purpose

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price: float) -> None:
        self.__price = price


class PricingStrategy:
    def __init__(self, discountRate: float, taxRate: float, specialPricing: bool):
        self.__discountRate = discountRate
        self.__taxRate = taxRate
        self.__specialPricing = specialPricing

    def get_discountRate(self) -> float:
        return self.__discountRate

    def set_discountRate(self, discountRate: float) -> None:
        self.__discountRate = discountRate

    def get_taxRate(self) -> float:
        return self.__taxRate

    def set_taxRate(self, taxRate: float) -> None:
        self.__taxRate = taxRate

    def is_specialPricing(self) -> bool:
        return self.__specialPricing

    def set_specialPricing(self, specialPricing: bool) -> None:
        self.__specialPricing = specialPricing

    def calculate_price(self, base_price: float, visitor_category: VisitorCategory, age: int = None) -> float:
        if self.__specialPricing:
            return base_price - (base_price * self.__discountRate) + (base_price * self.__taxRate)
        else:
            if visitor_category == VisitorCategory.Adult and 18 <= age <= 60:
                return 63.00 + (63.00 * self.__taxRate)
            elif visitor_category in [VisitorCategory.Child, VisitorCategory.Teacher, VisitorCategory.Student, VisitorCategory.Senior]:
                return 0.00  # Free ticket for children, teachers, students, and seniors
            elif visitor_category == VisitorCategory.Group:
                return (base_price / 2) + ((base_price / 2) * self.__taxRate)  # 50% discount for groups
            else:
                return base_price + (base_price * self.__taxRate)

def test_artwork_addition():
    # Test addition of new artwork to the museum
    location = Location("Gallery 1", LocationType.PermanentGallery)
    artwork = Artwork("Mona Lisa", "Leonardo da Vinci", datetime(1503, 1, 1), "An archetypal masterpiece of the Italian Renaissance", location)
    print(f"New artwork added to the museum: {artwork.get_title()}")
    print(f"Artist: {artwork.get_artist()}")
    print(f"Date of Creation: {artwork.get_dateOfCreation().strftime('%Y-%m-%d')}")
    print(f"Historical Significance: {artwork.get_historicalSignificance()}")
    print(f"Location: {artwork.get_location().get_name()}\n")

def test_exhibition_opening():
    # Test opening of a new exhibition at the museum
    location = Location("Gallery 1", LocationType.PermanentGallery)
    exhibition = Exhibition("Travelling through Fables", datetime(2024, 3, 26), datetime(2024, 7, 21), location, "Ahmed Al")
    print("New exhibition opened at the museum:", exhibition.get_name())

def test_ticket_purchase_individual():
    # Test ticket purchase for an individual
    location = Location("Gallery 1", LocationType.PermanentGallery)
    visitor = Visitor("Dana", "Dana@gmail.com", 25, VisitorCategory.Adult)
    pricing_strategy = PricingStrategy(0.0, 0.05, False)
    ticket = visitor.purchase_ticket(exhibition, pricing_strategy, 63.00)
    print("Ticket purchased by", visitor.get_name(), "for", ticket.get_eventName(), "at", ticket.get_location().get_name(), "for the price of", ticket.get_price())

def test_ticket_purchase_group():
    # Test ticket purchase for a group
    location = Location("Gallery 1", LocationType.PermanentGallery)
    group = Visitor("Sara's Group member", "Sara@gmail.com", 25, VisitorCategory.Group)
    pricing_strategy = PricingStrategy(0.5, 0.05, False)
    ticket = group.purchase_ticket(exhibition, pricing_strategy, 63.00)
    print("Tickets purchased by", group.get_name(), "for", ticket.get_eventName(), "at", ticket.get_location().get_name(), "for the price of", ticket.get_price(), "(Original Price: 63.00, Discounted Price:", ticket.get_price(), ")")

def test_display_payment_receipt():
    # Test display of payment receipt
    location = Location("Gallery 1", LocationType.PermanentGallery)
    visitor = Visitor("Dana", "Dana@gmail.com", 25, VisitorCategory.Adult)
    pricing_strategy = PricingStrategy(0.0, 0.05, False)
    ticket = visitor.purchase_ticket(special_event, pricing_strategy, 100.00)
    print(f"Payment receipt for: {visitor.get_name()}")
    print(f"Purchase Date: {ticket.get_date().strftime('%Y-%m-%d %H:%M')}")
    print(f"Event: {ticket.get_eventName()}")
    print(f"Location: {ticket.get_location().get_name()}")
    print(f"Category: {ticket.get_category().name}")
    print(f"Price: AED {ticket.get_price():.2f}\n")

if __name__ == "__main__":
    print("\nTesting Artwork Addition:")
    test_artwork_addition()
    print("\nTesting Exhibition Opening:")
    test_exhibition_opening()

    # Additional setup for testing ticket purchase
    exhibition = Exhibition("Travelling through Fables", datetime(2024, 3, 26), datetime(2024, 7, 21), Location("Gallery 1", LocationType.PermanentGallery), "Ahmed Al")
    special_event = SpecialEvent("Special Event: Cartier Dialouge", datetime(2024, 4, 1), datetime(2024, 4, 1), Location("Outdoor Area", LocationType.OutdoorSpace), "Sponsors Inc.", "Celebration", 100.00)

    print("\nTesting Ticket Purchase for Individual:")
    test_ticket_purchase_individual()
    print("\nTesting Ticket Purchase for Group:")
    test_ticket_purchase_group()
    print("\nTesting Display Payment Receipt:")
    test_display_payment_receipt()
