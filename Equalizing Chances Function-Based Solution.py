# Write your code here
import random


def get_winner_for(opponent):
    dic = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}
    return dic[opponent]


def computer_choice():
    return random.choice(['rock', 'scissors', 'paper'])


def compare_both(user, computer):
    value = {'rock': 5, 'scissors': 4, 'paper': 3}
    user = value[user]
    option = computer
    computer = value[computer]

    # player1 - player2 => win -> 1, -2 | lose -> 2, -1 | draw -> 0

    if user - computer == 1 or user - computer == -2:
        return 'Well done. The computer chose '+str(option)+' and failed'
    elif user - computer == 2 or user - computer == -1:
        return 'Sorry, but the computer chose '+str(option)
    else:
        return 'There is a draw ('+str(option)+')'


user_choice = input().strip()
print(compare_both(user_choice, computer_choice()))

# print('Sorry, but the computer chose', get_winner_for(user_choice)) #SOlution for stage 1
