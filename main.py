print "Hello!"

print 'Let\'s get started'

# Another way to do the same thing but using double quotes
# Instead of single quotes, notice how line 8 below doesn't need \ to escape the ' in what's up.

# print "I hope you are doing well today. What's up?"



spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")


if len(spy_name) > 0:


    # String Concatenation using + symbol
    print 'Welcome ' + spy_name + '. Glad to have you back with us.'

    spy_salutation = raw_input("Should I call you Mister or Miss?: ")

    # Variable has been updated
    spy_name = spy_salutation + " " + spy_name

    print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."


    # Let's create some new variables
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_age = raw_input("What is your age?")

    # Raw input always gives us a string
    print type(spy_age)

    spy_age = int(spy_age)

    # Age cannot be less than 12 and no spies greater than 50 are allowed to exist
    # Nested if
    if spy_age > 12 and spy_age < 50:

        spy_rating = raw_input("What is your spy rating?")
        spy_rating = float(spy_rating)

        if spy_rating > 4.5:
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'

        # Let's make this spy come online
        spy_is_online = True

        #One final message with all the details
        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"

        #Better Way of doing this
        #print "Authentication complete. Welcome %s, age: %d and rating of: %f. Proud to have you onboard" % (spy_name, spy_age, spy_rating)

        #Best way of doing this
        #print "Authentication complete. Welcome %s, age: %d and rating of: %.2f. Proud to have you onboard" % (spy_name, spy_age, spy_rating)

    else:
        print 'Sorry you are not of the correct age to be a spy'


else:

    print "A spy needs to have a valid name. Try again please."
