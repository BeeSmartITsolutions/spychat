from spy_details import spy, friends
from steganography.steganography import Steganography
from datetime import datetime

STATUS_MESSAGES = ['My name is X, Mr. X', 'Work in Silence, let your success make the noise', 'Never Give Up']

friends = []
print "Hello! Let\'s get started"

question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? "
existing = raw_input(question)

def add_status(current_status_message):

    updated_status_message = None

    
    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

   
    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

       
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if current_status_message:
        print 'Your updated status message is: %s' % (current_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

def add_friend():
       new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }

    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")

    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = raw_input("Age?")
    new_friend['age'] = int(new_friend['age'])

    new_friend['rating'] = raw_input("Spy rating?")
    new_friend['rating'] = float(new_friend['rating'])
  
     if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends_name)

def select_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend['name'],
                                                   friend['age'],
                                                   friend['rating'])
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1
    
    return friend_choice_position

def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_choice]['chats'].append(new_chat)

    print "Your secret message image is ready!"


def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)

    print "Your secret message has been saved!"

def start_chat(spy_name, spy_age, spy_rating):


    current_status_message = None


    spy_name = spy['salutation'] + " " + spy['name']


    if spy_age > 12 and spy_age < 50:


        print "Authentication complete. Welcome " + spy['name'] + " age: " + str(spy['age']) + " and rating of: " + str(spy['rating']) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing == "Y":
    start_chat(spy['name'],spy['age'], spy['rating'])
else:

    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    spy['salutation'] = raw_input("Should I call you Mr. or Ms.?: ")

    spy['age'] = raw_input("What is your age?")
    spy['age'] = int(spy['age'])

    spy['rating'] = raw_input("What is your spy rating?")
    spy['rating'] = float(spy['rating'])

    spy_is_online = True

    start_chat(spy['name'], spy['age'], spy['rating'])
