from enum import Enum

class VisitorCategory(Enum):
    Adult = 1
    Child = 2
    Teacher = 3
    Student = 4
    Senior = 5
    Group = 6

class Visitor:
    def __init__(self, name: str, email: str, age: int, category: VisitorCategory):
        self.name = name
        self.email = email
        self.age = age
        self.category = category
        self.tickets = []
    # Getter and Setter methods...
