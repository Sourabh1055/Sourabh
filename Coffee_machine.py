Menu = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 130
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee" : 24,
        },
        "cost": 210,
    },  
    "cappuccino": {
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 260
    }
}
profit = 0
resources = {
    "water": 2000,
    "milk": 1000,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    print("Please insert coins.")
    total = int(input("how many ₹10 coins: ")) * 10 
    total += int(input("how many ₹5 coins: ")) * 5
    total += int(input("how many ₹2 coins: ")) * 2
    total += int(input("how many ₹1 coins: ")) * 1
    return total 

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ₹{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}") 

is_on = True
while is_on:
    drink = input("What would you like?(espresso,latte,cappuccino): ").lower()
    if drink == "off":
        is_on = False
        print("Under maintanance.")
    elif drink == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    elif drink in Menu:
        choice = Menu[drink]
        print(f"The price of {drink} is ₹{choice['cost']}")
        if is_resource_sufficient(choice["ingredients"]):
            payment = process_coin() 
            if is_transaction_successful(payment, choice["cost"]):
                make_coffee(drink, choice["ingredients"])
    
    else:
            print("Invalid choice. Please choose espresso, latte, or cappuccino.")