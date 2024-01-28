# Ask your users to list a bunch of information about them: things they like, things they hate, names of family and friends...
# It's up to you how many and what kinds of things you pick. Keep it wacky!

# Now construct your story - it can be about anything you want, but must use the variables you've created in step 1.

# Make sure to only work one paragraph at a time. Otherwise things could get a bit messy.

print("Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!")

name = input("What is your name? > ")
enemy = input("What is your worst enemy’s name? > ")
superpower = input("What is your superpower? > ")
home = input("Where do you live? > ")
food = input("What is your favorite food? > ")

print("Hello","\033[32m", name,"\033[0m", "! Your ability to", "\033[31m", superpower, "\033[0m", "will make sure you never have to look at","\033[33m", enemy,"\033[0m", "again. Go eat","\033[36m", food,"\033[0m", "as you walk down the streets of","\033[34m", home,"\033[0m", "and use","\033[31m", superpower,"\033[0m", "for good and not evil!")
