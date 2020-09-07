from random import choice

name = input('Enter your name: ')
print('Hello, ' + name)

score = 0

rating_dict = {}

with open('rating.txt') as f:
    for line in f:
        (key, val) = line.split()
        rating_dict[key] = val

if name in rating_dict:
    score = rating_dict[name]
else:
    score = 0
       

vars = ['scissors', 'rock', 'paper']
wins = ['paperrock', 'scissorspaper', 'rockscissors']


while True:
    user = input('Your move: ')
    if user == '!exit':
        print('Bye!')
        break
    if user == '!rating':
        print(f'Your rating: {score}')
        break
    comp = choice(vars)

    if user == comp:
         print(f'There is a draw ({comp})')
         score = score + 50
    elif user + comp in wins:
        print(f'Well done. Computer chose {comp} and failed')
        score = score + 100
    else:
        print(f"Sorry, but computer chose {comp}")
         
    if user not in vars and user != '!exit':
        print('Invalid input')
    
  
