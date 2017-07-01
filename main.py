from spy_details import spy_name, spy_salutation, spy_rating, spy_age, spy_is_online

print "Hello! Let\'s get started"

question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? "
existing = raw_input(question)

spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

def start_chat(spy_name,spy_age, spy_rating):

    current_status_message = None


    spy_name = spy_salutation + " " + spy_name

    
    if spy_age > 12 and spy_age < 50:

        
        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"


        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

          
                if menu_choice == 1:
                    print 'You chose to update the status'
                else:
                    show_menu=False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing == "Y":
    start_chat(spy_name,spy_age, spy_rating)
else:
    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False


    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    
    if len(spy_name) > 0:
        spy_salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy_age = raw_input("What is your age?")
        spy_age = int(spy_age)

        spy_rating = raw_input("What is your spy rating?")
        spy_rating = float(spy_rating)

        spy_is_online = True

        start_chat(spy_name, spy_age, spy_rating)
    else:
        print 'Please add a valid spy name'
