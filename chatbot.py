# This file contains the PizzeriaChatBot class which handles the order processing.

from menu import menu

class PizzeriaChatBot:
    def __init__(self):
        self.menu = menu
        self.order = []
        self.total = 0

    def parse_order(self, item, size=None):
        item = item.lower()  # Convert to lowercase for consistent comparison
        normalized_menu = {k.lower(): v for k, v in self.menu.items()}
        normalized_toppings = {k.lower(): v for k, v in self.menu["toppings"].items()}
        normalized_drinks = {k.lower(): v for k, v in self.menu["drinks"].items()}
        normalized_menu["toppings"] = normalized_toppings
        normalized_menu["drinks"] = normalized_drinks

        if item in normalized_menu:
            if isinstance(normalized_menu[item], dict):  # If the item has sizes
                if size in normalized_menu[item]:
                    price = normalized_menu[item][size]
                    self.order.append((item, size, price))
                    self.total += price
                    return f"Added {size} {item} to your order. Current total is ${self.total:.2f}."
                else:
                    return f"{item} is available in the following sizes: {', '.join(normalized_menu[item].keys())}."
            else:
                price = normalized_menu[item]
                self.order.append((item, None, price))
                self.total += price
                return f"Added {item} to your order. Current total is ${self.total:.2f}."
        elif item in normalized_menu["toppings"]:
            price = normalized_menu["toppings"][item]
            self.order.append((item, None, price))
            self.total += price
            return f"Added {item} topping to your order. Current total is ${self.total:.2f}."
        elif item in normalized_menu["drinks"]:
            if size in normalized_menu["drinks"][item]:
                price = normalized_menu["drinks"][item][size]
                self.order.append((item, size, price))
                self.total += price
                return f"Added {size} {item} to your order. Current total is ${self.total:.2f}."
            else:
                return f"{item} is available in the following sizes: {', '.join(normalized_menu['drinks'][item].keys())}."
        else:
            return f"Item {item} is not available. Please choose from the menu."

    def get_order(self):
        return self.order

    def get_total(self):
        return self.total

    def reset_order(self):
        self.order = []
        self.total = 0
        return "Order has been reset."