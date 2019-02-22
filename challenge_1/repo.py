import items

menu = []
def show_menu():
    return menu

def add_item(meal_number, name, description, ingredients, price):
    m = items.MenuItems(meal_number, name, description, ingredients, price)
    menu.append(m)

def delete_item(name):
    for item in menu:
        if name == item.name:
                index = menu.index(item)
                del menu[index]
                return True


