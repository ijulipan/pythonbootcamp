#Important: Please refer to to the Coffee Machine PDF documentation to understand the usages of these classes and objects

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()



is_machine_on = True

while is_machine_on is True:
    user_choice = input(f"What would you like? ({menu.get_items()}): ") 
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)
        else:
            is_machine_on = False

