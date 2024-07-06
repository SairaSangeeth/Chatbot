# This file contains the main script to run the pizzeria chatbot.

from chatbot import PizzeriaChatBot

def main():
    bot = PizzeriaChatBot()
    print("Welcome to the Pizzeria Chatbot!")
    print("You can order multiple items in one line, separated by commas.")
    print("For example: 'pepperoni pizza large, coke medium'")
    
    while True:
        user_input = input("Enter your order (or type 'done' to finish): ").strip().lower()
        if user_input == "done":
            break

        orders = user_input.split(",")  # Split input by commas to handle multiple items

        for order in orders:
            parts = order.strip().split()
            if parts[-1] in ["large", "medium", "small"]:
                item = " ".join(parts[:-1])
                size = parts[-1]
            else:
                item = " ".join(parts)
                size = None
            response = bot.parse_order(item, size)
            print(response)

    print("Your final order:")
    for order_item in bot.get_order():
        print(order_item)
    print(f"Final total: ${bot.get_total():.2f}")
    print(bot.reset_order())

if __name__ == "__main__":
    main()