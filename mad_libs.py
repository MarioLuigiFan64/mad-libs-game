# Mad Libs Game in Python

# 1. Ask the user for words
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")

# 2. Create the story
story = (
    f"One day, a {adjective} {animal} decided to {verb} at the {place}. "
    f"Everyone was surprised to see a {animal} with a {noun}!"
)

# 3. Show the result
print("\nHere is your Mad Libs story!")
print(story)