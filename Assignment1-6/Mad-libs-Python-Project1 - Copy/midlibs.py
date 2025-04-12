# Mad Libs Game

name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a food item: ")
verb = input("Enter a verb: ")

# Mad Libs story
story = f"One day, {name} went to {place}. There, they saw a {animal} eating {food}. " \
        f"{name} was so surprised that they started to {verb}!"

# Story print 
print("\nHere is your Mad Libs story:\n")
print(story)
