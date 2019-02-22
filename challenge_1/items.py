
class MenuItems:

    def __init__ (self, meal_number, name, description, ingredients, price):
        self.meal_number = meal_number
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.price = price

    def __repr__(self):
        return self.name
