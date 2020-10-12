from pizza import Pizza
from pizzasize import PizzaSize

# This function shows a limitation on tool-assisted
# refactoring in a dynamic language like Python.
#
# When you rename the Pizza getPrice method to get_price,
# does it rename the method here?
# - if no type annotation on the pizza parameter, maybe not
# - if use type annotation ':Pizza' on the parameter, it should

if __name__ == "__main__":
    pizza = Pizza(PizzaSize.small)
    pizza.add_topping("mushroom")
    pizza.add_topping("tomato")
    pizza.add_topping("pinapple")
    pizza.print_pizza(pizza)

    pizza2 = Pizza(PizzaSize.medium)
    pizza.print_pizza(pizza2)

    pizza3 = Pizza(PizzaSize.large)
    pizza3.add_topping("seafood")
    pizza.print_pizza(pizza3)
