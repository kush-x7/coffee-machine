menu = {                            # ->created a dictionary
    "black-coffee":                 # -> key with name black coffee
        {                           # menu= {"key": {"key":{"key":value, "2key":value}}}
            "ingredients":          # -> created a dict in place of value of black=coffee
                {
                    "water": 50,    # ->one more dict with key ->water , ->value ->50
                    "coffee": 18
                },
            "cost":10
        },

    "latte":
        {
            "ingredients":
                {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24
                },
            "cost": 15
        },

    "cappuccino":
        {
            "ingredients":
                {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24
                },
            "cost": 20
        },
}

total_resource = {"water": 500, "milk": 250, "coffee": 100}


def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= total_resource[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    """Return total amount inserted"""
    print("Please insert coins.")
    total = int(input("How many one rupees coin? "))
    total += int(input("How many 5 rupees coin? ")) *5
    total += int(input("How many 10 rupees coin | notes? ")) * 10
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received-drink_cost
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffe(drink_name, order_ingredient):
    """Deduct the required ingredient"""
    for item in order_ingredient:
        total_resource[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}")


profit = 0
show = True
while show:
    user_choice = input("What would you like? (black-coffee/latte/cappuccino)  ||or wanna print report ||off ->").lower()
    if user_choice == "off":
        show = False
    elif user_choice == "report":
        print(f"water-> {total_resource['water'] }")
        print(f"Milk-> {total_resource['Milk'] }")
        print(f"Coffee->{total_resource['Coffee'] }")
        print(f"Money-> Rs{ profit}")
    else:
        drink = menu[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(user_choice, drink["ingredients"])





