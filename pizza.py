from pizzasize import PizzaSize

class Pizza:
    """A pizza with a size and optional toppings."""
    
    def __init__(self, size: PizzaSize):
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        price = self.size.value['price'] + self.size.value['topping']*len(self.toppings)

        return price

    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def print_pizza(self, pizza):
        """
        Print a description of a pizza, along with its price.
        """

        print(f"A {str(pizza)}")
        print("Price:", pizza.get_price())
    
    def __str__(self):
        # create printable description of the pizza such as
        # "small pizza with muschroom" or "small plain pizza"
        description = self.size.name
        if self.toppings:
            description += " pizza with "+ ", ".join(self.toppings)
        else:
            description += " plain pizza"
        return description
