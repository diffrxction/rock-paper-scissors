import random
user_choice = input()

options = {"rock": "paper",
           "paper": "scissors",
           "scissors": "rock"}

ai_choice = random.choice(list(options.keys()))

if user_choice == ai_choice:
    print(f"There is a draw ({ai_choice})")
    
elif user_choice != options[ai_choice]:
    print(f"Sorry, but the computer chose {ai_choice}")
    
elif user_choice == options[ai_choice]:
    print(f"Well done. The computer chose {ai_choice} and failed")
