class Pizza:
    """A pizza with a size and optional toppings."""
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

    def __init__(self, size):
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        if self.size == self.SMALL:
            price = 120 + 20*len(self.toppings)
        elif self.size == self.MEDIUM:
            price = 200 + 25*len(self.toppings)
        elif self.size == self.LARGE:
            price = 280 + 30*len(self.toppings)
        else:
            raise ValueError("Unknown pizza size "+self.size)
        return price

    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def print_pizza(self, pizza):
        """
        Print a description of a pizza, along with its price.
        """
        # create printable description of the pizza such as
        # "small pizza with muschroom" or "small plain pizza"
        description = pizza.size
        if pizza.toppings:
            description += " pizza with "+ ", ".join(pizza.toppings)
        else:
            description += " plain pizza"
        print(f"A {description}")
        print("Price:", pizza.get_price())
