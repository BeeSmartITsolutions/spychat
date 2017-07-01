print "Hello!"

print 'Let\'s get started'

# Another way to do the same thing but using double quotes
# Instead of single quotes, notice how line 8 below doesn't need \ to escape the ' in what's up.

# print "I hope you are doing well today. What's up?"



spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")


print 'Welcome ' + spy_name + '. Glad to have you back with us.'

spy_salutation = raw_input("Should I call you Mister or Miss?: ")

spy_name = spy_salutation + " " + spy_name

print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."
