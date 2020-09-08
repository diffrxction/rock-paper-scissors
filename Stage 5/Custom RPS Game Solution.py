# Write your code here
import random

# Enter name
name = input('Enter your name: ')
print("Hello, " + name, end="!")

# Enter list of options
options = input()

# If nothing is entered, original rock, paper scissors starts:
if options == "":
    options = "rock,paper,scissors"
valid_options = options.split(sep=',')  # Splitting string into a list

# Reading rating.txt, storing as a list and removing line breaks
f = open('rating.txt', 'r+')
rating = f.readlines()
f.close()

rating = [i.strip("\n") for i in rating]

# Creating key-value pairs dictionary for names and ratings to look like {'Tim': '350', 'Jane': '200', 'Alex': '400'}:
rating_dict = {}

for i in rating:
    rating_dict[i.split(' ')[0]] = i.split(' ')[1]

# Checking if name is in the keys:
name_exists = name in rating_dict.keys()

# If name exists in the rating.txt file, take starting rating from the file. Otherwise set at 0:
if name_exists:
    game_rating = int(rating_dict[name])
else:
    game_rating = 0
# Line 30-36 could be reduced but I'm too exhausted to spend a minute on it.

# Playing the game
print("Okay, let's start")
while True:
    pick = input()
    if pick == "!exit":
        print("Bye!")
        break
    elif pick == "!rating":
        print("Your rating: " + str(game_rating))
        continue
    elif pick not in valid_options:
        print("Invalid input")
        continue
    else:
    
    # This is the rotation of custom list. where we treat a linear list as a circle. This was the key concept required to solve this stage.
    
        comp = random.choice(valid_options)
        index_pick = valid_options.index(pick)
        before = valid_options[:index_pick]
        after = valid_options[index_pick + 1:]
        new_list = after + before
        half = int(len(new_list) / 2)
        comp_wins = new_list[:half]
        if pick == comp:
            print("There is a draw " + comp)
            game_rating += 50
        elif comp in comp_wins:
            print("Sorry, but the computer chose " + comp)
        else:
            print("Well done. The computer chose " + comp + " and failed")
            game_rating += 100
