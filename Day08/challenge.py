# Affirmations (or insults) Generator
# Today's focus is using all the skills you have learned so far:
# 
# - input and output
# - concatenation
# - if statements
# - nested if statements
# 
# Build a custom affirmations generator to give the user a customized affirmation each day of the week.
# Make sure you ask the user for their name, the current day of the week, and a few of their favorite things. All of this information should be used to help you build your affirmations.
# The goal is to generate a unique message for each day of the week based on the user's answers.
# Use concatenation to generate the affirmation.
# If affirmations are not your jam, then you could do a daily joke or insult. Please don't be mean. Keep it light and funny.
# Final challenge: Can you create if statements that do not care about capital or lowercase letters of names.

# Useful web resources:
# - https://www.w3schools.com/python/python_ref_string.asp
# - https://ioflood.com/blog/python-concatenate-strings/#:~:text=The%20simplest%20way%20to%20concatenate,str1%20%2B%20'%20'%20%2B%20str2%20.&text=In%20this%20example%2C%20we've,using%20the%20'%2B'%20operator.

print("=== DAILY AFFIRMATIONS GENERATOR ===")
nameRaw = input("What do you like to be known as? > ")
name = nameRaw.title()

print()
print("Nice to meet you",name)
dowRAW = input("What day is it today? > ")
dow = dowRAW.title()

if dow == "Monday":
    msg = 'It\'s only the start of the week {}! You\'ve still got a long way to go.'.format(name)
    print(msg)
elif dow == "Tuesday":
    print("TODO")
elif dow == "Wednesday":
    print("TODO")
elif dow == "Thursday":
    print("TODO")
elif dow == "Friday":
    msg = 'On more day {} and then it\'s the weekend.'.format(name)
    print(msg)
elif dow == "Saturday":
    msg = 'Yay! You made it to the weekend {}. I hope you have fun plans.'.format(name)
    print(msg)
elif dow == "Sunday":
    msg = 'Make sure you rest well today {}. Back to work tomorrow.'.format(name)
    print(msg)
else:
    msg = 'That\'s not a day of the week! - {}'.format(dow)
    print(msg)