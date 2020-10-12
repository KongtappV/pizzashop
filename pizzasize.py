""" Enumeration of pizza sizes """
from enum import Enum

class PizzaSize(Enum):
    small = {"price": 120, "topping": 20}
    medium = {"price": 200, "topping": 25}
    large = {"price": 280, "topping": 30}

    def __str__(self):
        return self.name.title()

if __name__ == "__main__":
    for size in PizzaSize:
        print(size, "pizza is", size.value['price'], "plus topping", size.value['topping'])