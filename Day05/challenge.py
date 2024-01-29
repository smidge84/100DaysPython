# "Which character are you?" Generator
# Ask your users a series of questions that identify if they're one of the characters in the world you have created.
# Add multiple if statements to check the result of each question.
# Make sure to have a final print if they haven't selected any of the characters so far.

print("=== Marvel Movie Character Creator ===")

spiderman = input("Do you like 'hanging around'? > ")

if spiderman == "yes":
    print("You must be the amazing Spiderman!")
else:
    print("Then you're not Spider-man")

    korg = input("Do you have a 'gravelly' voice? > ")

    if korg == "yes":
        print("You're the mighty Korg!")
    else:
        print("Aww, then you're not Korg")

        marvel = input("Do you often feel 'Marvelous'? > ")

        if marvel == "yes":
            print("Aha! You're Captain Marvel! Hi!")
        else:
            print("Sorry! You must not be a superhero!")
