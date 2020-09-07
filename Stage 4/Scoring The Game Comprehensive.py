import random
name = input('Enter your name: ')
print(f'Hello, {name}')
rating = {key: int(val) for key, val in [line.split() for line in open("rating.txt", "r")]}
while True:
    options = {'paper': ['paper', 'scissors', 'rock'], 'scissors': ['scissors', 'rock', 'paper'],
               'rock': ['rock', 'paper', 'scissors']}
    human = input()
    if human == '!rating':
        print(f'Your rating: {rating[name]}')
        continue
    if human == '!exit': break
    elif human not in options.keys():
        print('Invalid input')
        continue
    result = random.randint(0, 2)
    comp = options[human][result]
    result_text = [f'There is a draw ({comp})', f'Sorry, but the computer chose {comp}',
                   f'Well done. The computer chose {comp} and failed']
    print(result_text[result])
    if result == 0: rating[name] += 50
    elif result == 2: rating[name] += 100
print('Bye!')
