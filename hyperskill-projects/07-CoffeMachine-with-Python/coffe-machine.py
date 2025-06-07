class CoffeeMachine:
    def __init__(self):
        self.machine = {
            "water": 400,
            "milk": 540,
            "coffee beans": 120,
            "disposable cups": 9,
            "money": 550
        }
        self.state = "waiting"
        self.fill_step = 0
        self.temp_inputs = {}

    def handle_input(self, user_input: str):
        if self.state == "waiting":
            return self._handle_main_menu(user_input)

        elif self.state == "choosing_coffee":
            return self._handle_coffee_choice(user_input)

        elif self.state == "filling":
            return self._handle_filling(user_input)

    def _handle_main_menu(self, action):
        if action == "buy":
            self.state = "choosing_coffee"
            return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"

        elif action == "fill":
            self.state = "filling"
            self.fill_step = 0
            return "Write how many ml of water you want to add:"

        elif action == "take":
            money = self.machine["money"]
            self.machine["money"] = 0
            return f"I gave you ${money}"

        elif action == "remaining":
            return self._get_status()

        elif action == "exit":
            self.state = "off"
            return "Shutting down."

        else:
            return "Unknown command. Please choose from: buy, fill, take, remaining, exit"

    def _handle_coffee_choice(self, choice):
        recipes = {
            "1": ({"water": 250, "coffee beans": 16, "disposable cups": 1}, 4),  # espresso
            "2": ({"water": 350, "milk": 75, "coffee beans": 20, "disposable cups": 1}, 7),  # latte
            "3": ({"water": 200, "milk": 100, "coffee beans": 12, "disposable cups": 1}, 6)  # cappuccino
        }

        if choice == "back":
            self.state = "waiting"
            return "Back to main menu."

        if choice in recipes:
            recipe, cost = recipes[choice]
            if self._can_make(recipe):
                self._make_coffee(recipe, cost)
                self.state = "waiting"
                return "I have enough resources, making you a coffee!"
            else:
                self.state = "waiting"
                return self.not_enough_msg

        return "Invalid option. Choose 1, 2, 3, or back."

    def _handle_filling(self, value):
        prompts = [
            "Write how many ml of water you want to add:",
            "Write how many ml of milk you want to add:",
            "Write how many grams of coffee beans you want to add:",
            "Write how many disposable cups you want to add:"
        ]
        keys = ["water", "milk", "coffee beans", "disposable cups"]

        try:
            value = int(value)
        except ValueError:
            return "Please enter a valid number."

        self.machine[keys[self.fill_step]] += value
        self.fill_step += 1

        if self.fill_step < len(prompts):
            return prompts[self.fill_step]
        else:
            self.state = "waiting"
            return "Resources added."

    def _can_make(self, recipe):
        for item, amount in recipe.items():
            if self.machine[item] < amount:
                self.not_enough_msg = f"Sorry, not enough {item}!"
                return False
        return True

    def _make_coffee(self, recipe, cost):
        for item, amount in recipe.items():
            self.machine[item] -= amount
        self.machine["money"] += cost

    def _get_status(self):
        return (
            f"\nThe coffee machine has:\n"
            f"{self.machine['water']} ml of water\n"
            f"{self.machine['milk']} ml of milk\n"
            f"{self.machine['coffee beans']} g of coffee beans\n"
            f"{self.machine['disposable cups']} disposable cups\n"
            f"${self.machine['money']} of money"
        )

machine = CoffeeMachine()
while True:
    if machine.state == "off":
        break
    if machine.state == "waiting":
        print("Write action (buy, fill, take, remaining, exit):")
    result = machine.handle_input(input())
    if result:
        print(result)





