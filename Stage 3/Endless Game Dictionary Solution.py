import random
options = {"rock": "paper",
           "paper": "scissors",
           "scissors": "rock"}

while True:
    # User choice and AI choice made within loop unlike previous stage.
    user_choice = input()
    ai_choice = random.choice(list(options.keys()))
    if user_choice == "!exit":
        print("Bye!")
        break
              
    if user_choice == ai_choice:
        print(f"There is a draw ({ai_choice})")
    
    elif user_choice != options[ai_choice]:
        print(f"Sorry, but the computer chose {ai_choice}")
    
    elif user_choice == options[ai_choice]:
        print(f"Well done. The computer chose {ai_choice} and failed")
    # User input is not exit command and absent in dict then input is Invalid   
    if not user_choice in options and user_choice != "!exit":
        print("Invalid input")
        
  
