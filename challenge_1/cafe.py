
import repo

while True:
    print("Komodo's Menu")
    user_input = input("1. Add Menu Item. \n"
                       "2. Show Menu. \n"
                       "3. Delete Menu Item. \n"
                       "4. Exit.\n")

    if user_input == "1":
        number = input('Enter Meal Number: ')
        meal = input("Enter Meal Name: ")
        meal_description = input("Describe the meal: ")
        ingredients = input("What are the ingredients: ")
        price = input("What is the price: ")
        repo.add_item(
            number, meal, meal_description, ingredients, price)
    elif user_input == "2":
        menu_list = repo.show_menu()
        print(menu_list)
    elif user_input == "3":
        try:
            meal_to_delete = input(
                'Enter the meal you want to delete from the menu: ')
            repo.delete_item(meal_to_delete)
        except Exception:
            print('Meal does not exist')
    elif user_input == "4":
        exit()
