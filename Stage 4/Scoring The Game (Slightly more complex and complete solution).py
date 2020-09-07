import random


def main():
    play()


def play():

    # load settings
    options, winner_loser_options = settings()

    # get player's name
    print("Enter your name: ", end="")
    player_name = input()
    print(f"Hello, {player_name}\n")

    user_score = get_score(player_name)
    # game loop
    while True:
        # get score in rating file
        try:
            player = input().lower().strip()
        except EOFError:
            print("EOFError")
            break

        if player == "exit!":
            print("Bye!")
            break

        elif player == "!rating":

            print(f"Your rating: {user_score[player_name]}")

        elif player in options:
            # random option for the comuser_score = get_score(player_name)puter
            bot = random.choice(options)

            # get the end game results into a list
            end_game = get_end_results(bot)

            # play the game
            result = game(player, bot, winner_loser_options, end_game)

            # scores
            if result == end_game[0]:
                user_score[player_name] += 100
            elif result == end_game[2]:
                user_score[player_name] += 50

            print(result)
        else:
            # message if player enter wrong choice
            print("Invalid input")


def get_score(player_name):
    # user with score dict
    user_with_score = dict()

    # read file
    file_name = "rating.txt"

    rating_file = open(file_name, "r")

    # check if user score is in the file

    for line in rating_file:
        parts = line.strip().split()
        name = parts[0]
        score = parts[1]
        if name == player_name:
            user_with_score[name] = int(score)
        else:
            user_with_score[player_name] = 0

    rating_file.close()

    return user_with_score


def get_end_results(bot):
    """[get ending result from bot option: draw win or lose]

    Args:
        bot (String): [the bot option]

    Returns:
        [List]: [List of Strings that will display ending of the game]
    """
    game_won = f"Well done. Computer chose {bot} and failed"
    game_lost = f"Sorry, but computer chose {bot}"
    draw = f"There is a draw ({bot})"

    end_game = [game_won, game_lost, draw]

    return end_game


def settings():
    """[game settings]

    Returns:
        [List, Dict]: [the options list and the winning conditions]
    """

    # list of the game options
    options = ['rock', 'paper', 'scissors']

    # dict: winning option (Key) : losing option (Value)
    winner_loser_options = {'rock': 'scissors',
                            'paper': 'rock',
                            'scissors': 'paper'}
    return options, winner_loser_options,


def game(player, bot, winner_loser_options, end_game):
    """ [play the game]

    Args:
        player (String): the player option (rock, paper, scissors) choice
        bot (String): the computer option (rock, paper, scissors) choice
        winner_loser_options (dict): winning option K to it's losing option V
        end_game (list): strings result to draw [-1], win [0] or lose [1]

    Returns:
        (String): the result of the match
    """

    if player == bot:
        return end_game[-1]
    if bot == winner_loser_options[player]:
        return end_game[0]
    return end_game[1]


main()
