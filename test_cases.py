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
