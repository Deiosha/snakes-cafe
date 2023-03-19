def main():
    """
    this is an example docstring
    :return: no return
    """
    name = input("What is your name? ")

    # we need to use an f string

    print(f"Hello {name}")
    menu = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
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
Unicorn Tears"""
    print(menu)

    prompt = """***********************************
** What would you like to order? **
***********************************"""

    finished_order = {}
    print(prompt)
    menu_item = input('Enter \'quit\'to quit: ')

    while menu_item != "quit":

        if menu_item in finished_order:
            complete_num = finished_order.get(menu_item) + 1
            finished_order.update({menu_item: complete_num})
        else:
            finished_order.update({menu_item: 1})

        print(finished_order)

        print(prompt)
        menu_item = input('Enter \'quit\' to quit: ')


if __name__ == "__main__":
    main()
