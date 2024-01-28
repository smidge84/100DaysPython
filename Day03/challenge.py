# Create these as a variable:
# A type of food
# A type of plant
# A method of cooking
# A word to describe burned food
# A household item

# Output a nice looking Recipe page that *concatenates* a dish in this format:
# cooking food with burned plant on a bed of item

food = input("Name a food > ")
plant = input("Name a plant > ")
cook = input("Name a cooking method > ")
burnt = input("What word describes burned food? > ")
tool = input("Name a DIY item > ")

print()
print("Tonight's dinner:")
print(cook, food, "with", burnt, plant, "on a bed of", tool, "s")
