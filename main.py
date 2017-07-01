import time

from colorama import Fore
from steganography.steganography import Steganography  # for using encode decode function

from spy_variable import spy, validate, Spy, ChatMessage, friends  # file_import

# default status message list

STATUS_MESSAGES = ['My name is X, Mr. X', 'Work in Silence, let your success make the noise', 'Never Give Up']


print "Hello! Let\'s get started"

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

# add status function start

def add_status():
    update_status_message = None

    if spy.current_status_message is not None:
        print 'Your current status message is %s \n' % spy.current_status_message
    else:
        print 'You don\'t have any status message currently \n'

    select = raw_input("Do you want to select from the older status (y/n)? ")

    if select.upper() == "N":
        new_status_message = raw_input("Please enter your status \t ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            update_status_message = new_status_message

    elif select.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nSelect form the messages above \t"))

        if len(STATUS_MESSAGES) >= message_selection:
            update_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you choose is not valid! Press either y or n.'

    if update_status_message:
        print 'Your updated status message is: %s' % (update_status_message)
    else:
        print 'You did not update your status message'

    return update_status_message


# add status function end


# add friends function start

def add_friend():
    new_friend = Spy('', '', 0, 0.0)

    valid = True

    while valid:

        new_friend.name = raw_input("Please add your friend's name: ")

        if len(new_friend.name) > 0:

            new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

            if len(new_friend.salutation) > 0:

                if new_friend.salutation == 'Mr.' or new_friend.salutation == 'mr.' or new_friend.salutation == 'ms.' or 'Ms.' == \
                        new_friend.salutation and new_friend.salutation != ' ':
                    new_friend.name = new_friend.salutation + " " + new_friend.name

                    new_friend.age = raw_input("Age?")

                    new_friend.age = int(new_friend.age)

                    if new_friend.age > 12 and new_friend.age < 50:

                        new_friend.rating = raw_input("Spy rating?")
                        new_friend.rating = float(new_friend.rating)

                        if new_friend.rating >= spy.rating:
                            friends.append(new_friend)
                            print 'Friend Added!'
                        else:
                            print 'You need to improve your rating.'
                    else:
                        print 'Sorry! We can\'t add spy. His age is not eligible for becoming spy'
                else:
                    print 'Sorry! Invalid entry. Please enter the specified salutation i.e., Mr. or Ms.'
            else:
                print 'OOPS!!!!.... You forgot to enter your Salutation or please enter a valid Salutation.....'
        else:
            print 'OOPS!!!!.... You forgot to enter your name.'

        valid = False

    return len(friends)


# add friends function end


# select friend function start

def select_a_friend():
    item_number = 1

    for friend in friends:
        print '%d %s %s whose age is %d with rating %.2f is online' % (
            item_number, friend.salutation, friend.name, friend.age, friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


# select friend function end


# send message function start

def send_message():
    friend_choice = select_a_friend()
    original_image = raw_input("What is the name of the image? \t")
    output_path = "secret_images\\output%s.jpg" % (original_image)
    text = raw_input("What do you want to say? \t")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


# send message function end


# read message function start

def read_message():
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file? \t")

    output_path = 'secret_images\\output%s.jpg' % (output_path)

    secret_text = Steganography.decode(output_path)
    if len(str(secret_text > 0 and secret_text < 100)):

        if secret_text == 'SOS' or secret_text == 'Sos' or secret_text == 'sos' or secret_text == 'SAVE ME' or secret_text == 'save me' or secret_text == 'Save Me':
            print 'You said ' + secret_text
            print '\n Its a special word and He/She is saying that He/She needs your help might be he/she is in Danger....'

        elif secret_text == 'Bb':
            print 'You said ' + secret_text
            print '\n Its a special word which means Bye Bye or Good Night....'

        elif secret_text == 'ty' or secret_text == 'TY' or secret_text == 'Ty' or secret_text == 'Thx' or secret_text == 'THX' or secret_text == 'thx':
            print 'You said ' + secret_text
            print '\n Its a special word which means Thank You or Thanks....'

        elif secret_text == 'TTYL' or secret_text == 'Ttyl' or secret_text == 'ttyl':
            print 'You said ' + secret_text
            print '\n Its a special word which means Talk To You Later....'

        elif secret_text == 'CYA' or secret_text == 'Cya' or secret_text == 'cya':
            print 'You said ' + secret_text
            print '\n Its a special word which means See You....'

        elif secret_text == 'Dunno' or secret_text == 'DUNNO' or secret_text == 'dunno':
            print 'You said ' + secret_text
            print '\n Its a special word which means Don\'t Know....'

        elif secret_text == 'Foad' or secret_text == 'FOAD' or secret_text == 'foad':
            print 'You said ' + secret_text
            print '\n Its a special word which means Fuck Off and Die....'

        elif secret_text == 'G2G' or secret_text == 'g2g' or secret_text == 'GTG' or secret_text == 'gtg' or secret_text == 'G2g' or secret_text == 'Gtg':
            print 'You said ' + secret_text
            print '\n Its a special word which means Got To Go or Got 2 Go....'

        elif secret_text == 'hand' or secret_text == 'Hand' or secret_text == 'HAND':
            print 'You said ' + secret_text
            print '\n Its a special word which means Have A Nice Day....'

        elif secret_text == 'HS' or secret_text == 'Hs' or secret_text == 'hs':
            print 'You said ' + secret_text
            print '\n Its a special word which means Holy shit....'

        elif secret_text == 'IC' or secret_text == 'ic' or secret_text == 'Ic':
            print 'You said ' + secret_text
            print '\n Its a special word which means I See....'

        elif secret_text == 'IMO' or secret_text == 'Imo' or secret_text == 'imo':
            print 'You said ' + secret_text
            print '\n Its a special word which means In My Opinion....'

        elif secret_text == 'ILY' or secret_text == 'Ily' or secret_text == 'ily' or secret_text == 'ILU' or secret_text == 'Ilu' or secret_text == 'ilu':
            print 'You said ' + secret_text
            print '\n Its a special word which means I Love You or I Love U....'

        elif secret_text == 'CUL' or secret_text == 'Cul' or secret_text == 'cul':
            print 'You said ' + secret_text
            print '\n Its a special word which means See You Later....'

        elif secret_text == 'SYS' or secret_text == 'sys' or secret_text == 'Sys' or secret_text == 'SUS' or secret_text == 'Sus' or secret_text == 'sus':
            print 'You said ' + secret_text
            print '\n Its a special word which means See You Soon....'

        elif secret_text == 'GN' or secret_text == 'Gn' or secret_text == 'gn' or secret_text == 'Gud 9ht':
            print 'You said ' + secret_text
            print '\n Its a special word which means Good Night....'

        elif secret_text == 'SD' or secret_text == 'Sd' or secret_text == 'sd':
            print 'You said ' + secret_text
            print '\n Its a special word which means Sweet Dreams....'

        elif secret_text == 'TC' or secret_text == 'tc' or secret_text == 'Tc':
            print 'You said ' + secret_text
            print '\n Its a special word which means Take Care....'

        else:
            print 'You said ' + secret_text

    elif len(str(secret_text > 100)):
        print 'You are talking too much please talk less otherwise you will get deleted'

    else:
        print 'There is no hidden text in you message'

    new_chat = ChatMessage(secret_text, False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


# read message function end


# read chat history function start

def read_chat_history():
    read_for = select_a_friend()

    print '\n'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print ('\033[1;34;40m ' + chat.time.strftime("%d %B %Y") + ' \033')
            print ('\033[1;31;40m You said: \033')
            print (Fore.BLACK + chat.message)
            print '\n'
        else:
            print (Fore.BLUE + chat.time.strftime("%d %B %Y"))
            print (Fore.RED + friends[read_for].name)
            print (Fore.BLACK + chat.message)
            print '\n'

# read chat history function start


# start applist function end

def start_applist(spy, password):
    spy.name = spy.salutation + " " + spy.name

    print "\n\nAuthentication complete. Welcome %s age: %s and rating of: %s ..... We are proud to have you with us" % (
        spy.name, str(spy.age), str(spy.rating))

    show_menu = True

    password1 = raw_input('\n\nPlease verify your self by entering your password...\t')

    if password1 == password:

        while show_menu:

            menu_choices = "\nWhat do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret " \
                           "message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n\n "
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    print '\nYou choose to update the status'
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    print '\nYou choose to add friends'
                    number_of_friends = add_friend()
                    print '\nYou have %d friends' % number_of_friends
                elif menu_choice == 3:
                    print '\nYou choose to send a message'
                    send_message()
                elif menu_choice == 4:
                    print '\nYou choose to read a message'
                    read_message()
                elif menu_choice == 5:
                    print '\nYou choose to read chat history'
                    read_chat_history()
                elif menu_choice == 6:
                    print'\n\nYou are about to exit in 5 seconds....'
                    s = 0
                    m = 0
                    h = 0
                    while s <= 5:
                        print h, 'Hours', m, 'Minutes', s, 'Seconds'
                        time.sleep(1)
                        s += 1
                        if s == 5:
                            exit()
                    show_menu = False
                else:
                    print'\nYou entered the wrong input. Please provide the input according to list.'
            else:
                print '\nYou haven\'t provided input. Please enter some input'
    else:
        print '\nYou entered a wrong password please enter correct one'
        print'\n\nYou are about to exit in 5 seconds....'
        s = 0
        m = 0
        h = 0
        while s <= 5:
            print h, 'Hours', m, 'Minutes', s, 'Seconds'
            time.sleep(1)
            s += 1
            if s == 5:
                exit()


# start applist function end


# main program start

print("Hi!!.. Welcome to spyChat")
print("Before preceding further, I would like to ask you about your choice\n")
question = "Do you want to continue as %s %s Y/N \t" % (spy.salutation, spy.name)
answer = raw_input(question)

if len(str(answer > 0)):

    password = raw_input('\n\nPlease enter your password for security...\t')

    if len(str(password > 0)):
        if answer.upper() == "Y":
            start_applist(spy, password)
        else:
            spy = Spy('', '', 0, 0.0)

            while validate:

                spy.name = raw_input("\n\nWelcome to spy chat, I would like to know your spy name first: \t")

                if len(spy.name) > 0:
                    spy.salutation = raw_input("\nShould I call you Mr. or Ms.?: \t")

                    if len(spy.salutation) > 0:

                        if spy.salutation == 'Mr.' or spy.salutation == 'mr.' or spy.salutation == 'ms.' or 'Ms.' == \
                                spy.salutation and spy.salutation != ' ':

                            spy.age = raw_input("\nWhat is your age?\t")
                            spy.age = int(spy.age)

                            if spy.age > 12 and spy.age < 50:

                                spy.rating = raw_input("\nWhat is your spy rating? (Rate yourself out of 5)\t")

                                spy.rating = float(spy.rating)

                                if spy.rating > 4.5:
                                    print '\n\nYou have an Excellent rating.'
                                elif spy.rating > 3.5 and spy.rating <= 4.5:
                                    print '\n\nYou are one of the good ones.'
                                elif spy.rating >= 2.5 and spy.rating <= 3.5:
                                    print '\n\nYou can do better.'
                                else:
                                    print '\n\nYou need to improve your rating.'

                                spy.is_online = True

                                validate = False

                                start_applist(spy, password)

                            else:
                                print "\n\nSORRY!!..Your age is not eligible for becoming spy"
                        else:
                            print "\n\nPlease enter the specified salutation i.e., Mr. or Ms."
                    else:
                        print "\n\nOOPS!!!!.... You forgot to enter your Salutation or please enter a valid Salutation....."
                else:
                    print "\n\nOOPS!!!!.... You forgot to enter your Name or please enter a valid spy name...."

