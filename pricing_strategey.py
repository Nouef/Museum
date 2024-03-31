from visitor import VisitorCategory

class PricingStrategy:
    def __init__(self, discount_rate: float, tax_rate: float, special_pricing: bool):
        self.discount_rate = discount_rate
        self.tax_rate = tax_rate
        self.special_pricing = special_pricing
 
    def calculate_price(self, base_price: float, visitor_category: VisitorCategory, age: int = None) -> float:
        if self.__specialPricing:
            return base_price - (base_price * self.__discountRate) + (base_price * self.__taxRate)
        else:
            if visitor_category == VisitorCategory.Adult and 18 <= age <= 60:
                return 63.00 + (63.00 * self.__taxRate)
            elif visitor_category in [VisitorCategory.Child, VisitorCategory.Teacher, VisitorCategory.Student, VisitorCategory.Senior]:
                return 0.00  # Free ticket for children, teachers, students, and seniors
            elif visitor_category == VisitorCategory.Group:
                return (base_price / 2) + ((base_price / 2) * self.__taxRate)  # 50% discount for groups
            else:
                return base_price + (base_price * self.__taxRate)
  # Getter and Setter methods...
