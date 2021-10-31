print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menuFood below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
""")

menuFood = [
    "Wings",
    "Cookies",
    "Spring Rolls",
    "Salmon", "Steak",
    "Meat Tornado",
    "A Literal Garden",
    "Ice Cream",
    "Cake",
    "Pie",
    "Coffee",
    "Tea",
    "Unicorn Tears"
]
counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sel_order = input(">")


def get_order(counter, sel_order, menuFood):
    while sel_order != "quit":
        if sel_order in menuFood:
            counter[menuFood.index(sel_order)] += 1
            print(
                f"{counter[menuFood.index(sel_order)]} order of {sel_order} have been added to your meal ")
        else:
            print(
                "This order is not on the menuFood ,Please Choose Something From The Menu")
        sel_order = input('>')


get_order(counter, sel_order, menuFood)
