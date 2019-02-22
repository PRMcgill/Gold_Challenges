import repo

while True:
    print("Komodo's Outing")
    user_input = input('Menu: \n'
                       '1. List all outings. \n'
                       '2. Add outing. \n'
                       '3. Calculate total price. \n'
                       '4. Calculate price per event. \n'
                       '5. Exit. \n')
    if user_input == '1':
        e_list = repo.Menu_functions()
        x = e_list.show_outings()
        print(x)

    elif user_input == '2':
        event_name = input('What is the event? ')
        attendence = input('How many people are attending? ')
        date_of_event = input(
            'What is the date of the event (mm/dd/yyyy)? ')
        per_person_cost = input('What is the total cost per person? ')
        
        new_outing = repo.Menu_functions()
        new_outing.add_outing(event_name, attendence,
                              date_of_event, per_person_cost)

    elif user_input == '3':
        q = 0
        for i in repo.outings:
            q += float(i.cost_per_person) * int(i.people_attending)
        print(f'The total cost is ${q}')
        

    elif user_input == '4':
        print(repo.outings)
        y = input('What event do you want the price for?: \n')
        for outing in repo.outings:
            if y == outing.event_type:
                print(
                    f'All {outing.event_type} outings cost ${int(outing.people_attending) * float(outing.cost_per_person)}.\n'
                    f'The cost per person for {outing.event_type} is ${outing.cost_per_person}')

    elif user_input == '5':
        exit()
    else:
        print('Enter a correct option')
