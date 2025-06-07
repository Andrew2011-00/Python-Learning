class VendingMachine:
    def __init__(self):
        self.machine = {
            "chips" : {"price" : 1.50, "stock" : 5},
            "soda" : {"price" : 2.00, "stock" : 3},
            "candy" : {"price" : 1.00, "stock" : 10}
        }

        self.state = "waiting"
        self.pending_product = None
        self.filling_item = 0
        self.money = 0.00
    def user_actions(self, input_str):
        if self.state == "waiting":
            return self.main_menu(input_str)

        elif self.state == "filling":
            return self._handle_filling(input_str)

        elif self.state == "pending_product":
            result = self._handle_choice(input_str)
            return result


    def main_menu(self, action):
        if action == "buy":
            self.state = "pending_product"
            return (f"""
            What do you want to buy?
            chips - $1.50 ({self.machine["chips"]["stock"]} left),
            soda - $2.00 ({self.machine["soda"]["stock"]} left),
            candy - $1.00 ({self.machine["candy"]["stock"]} left):
            """)

        elif action == "fill":
            self.state = "filling"
            self.filling_item = 0
            return "How many chips do you want to add?:"

        elif action == "take":
            money = self.money
            self.money = 0.00
            return f"I gave you ${money}"

        elif action == "remaining":
            return self.get_status()

        elif action == "exit":
            self.state = "off"
            return "Shutting Down."

        else:
            return "Unknown command. Please choose from: buy, fill, take, remaining, exit"

    def get_status(self):
        return (
            f"\nThe vending machine has:\n"
            f"chips - {self.machine['chips']["stock"]}\n"
            f"soda - {self.machine['soda']["stock"]}\n"
            f"candy - {self.machine['candy']["stock"]}\n"
            f"${self.money} of money\n"
        )

    def _handle_choice(self, choice):
        if self._can_buy(choice):
            self._buy_snacks(1, choice)
            self.state = "waiting"
            return f"I have enough stock, dispensing your {choice}!"
        else:
            self.state = "waiting"
            return self.not_enough_msg

    def _can_buy(self, product):
        item = self.machine.get(product)
        if item is None:
            self.not_enough_msg = f"{product} is not available."
            return False

        if item["stock"] <= 0:
            self.not_enough_msg = f"Sorry, not enough {product}!"
            return False
        return True

    def _buy_snacks(self, amount, item):
        self.machine[item]["stock"] -= amount
        self.money += self.machine[item]["price"] * amount

    def _handle_filling(self, value):
        prompts = [
            "Write how many chips you want to add:",
            "Write how many sodas want to add:",
            "Write how many candies you want to add:",
        ]
        keys = ["chips", "soda", "candy"]

        try:
            value = int(value)
        except ValueError:
            return "Please enter a valid number."

        self.machine[keys[self.filling_item]]["stock"] += value
        self.filling_item += 1

        if self.filling_item < len(prompts):
            return prompts[self.filling_item]
        else:
            self.state = "waiting"
            self.filling_item = 0
            return "Resources added."

machine = VendingMachine()
while True:
    if machine.state == "off":
        break
    if machine.state == "waiting":
        print("Write action (buy, fill, take, remaining, exit):")
    result = machine.user_actions(input())
    if result:
        print(result)






