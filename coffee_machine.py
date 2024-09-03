from menu import menu
from resources import profit, resources


class CoffeeMachine:
    def __init__(self):
        self.resources = resources
        self.profit = profit
        self.is_on = True

    def check_resources(self, order_ingredients):
        for item in order_ingredients:
            if order_ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        coins_five = int(input("How many 5 cent coins?: "))
        coins_ten = int(input("How many 10 cent coins?: "))
        coins_twenty = int(input("How many 20 cent coins?: "))
        coins_fifty = int(input("How many 50 cent coins?: "))
        total = coins_five * 5 + coins_ten * 10 + coins_twenty * 20 + coins_fifty * 50
        return total

    def is_payment_successful(self, money_received, coffee_cost):
        if money_received >= coffee_cost:
            self.profit += coffee_cost
            change_money = money_received - coffee_cost
            print(f"Here is {change_money} cents in change.")
            return True
        else:
            print("Sorry, there is not enough money inserted.")
            return False

    def make_coffee(self, coffee_name, coffee_ingredients):
        for item in coffee_ingredients:
            self.resources[item] -= coffee_ingredients[item]
        print(f"Here is your {coffee_name} ☕️. Enjoy!")

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: {self.profit}c")

    def start(self):
        while self.is_on:
            customer_choice = input("What would you like? (espresso/latte/cappuccino): ")
            if customer_choice == 'off':
                self.is_on = False
            elif customer_choice == 'report':
                self.report()
            else:
                coffee_type = menu[customer_choice]
                if self.check_resources(coffee_type['ingredients']):
                    payment = self.process_coins()
                    if self.is_payment_successful(payment, coffee_type['cost']):
                        self.make_coffee(customer_choice, coffee_type['ingredients'])

                     
coffee_machine = CoffeeMachine()
coffee_machine.start()
