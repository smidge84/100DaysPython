# Make your own login program.
# Create a program where someone logins with their username and password correctly and then gets a lovely individual greeting.
# Write a specific personalized greeting for 3 different people.
# Don't forget an else statement for everyone else who shouldn't be logging in.

print("MY LOGIN SYSTEM")
print("+++++++++++++++")

username = input("Username > ")
password = input("Password > ")

if username == "mark" and password == "password":
    print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
    print("Hey there Suzanne!")
elif username == "rich" and password == "p4ssw0rd":
    print("You're the best, Rich!")
else:
    print("Go away!")
