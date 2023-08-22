import random

def choose_options():
    options = ('rock', 'paper', 'scissors')
    user_choice = input('Choose rock, paper or scissors: ')
    user_choice = user_choice.lower()

    if not user_choice in options:
        print('Invalid option')
        #continue
        return None, None

    computer_choice = random.choice(options)

    print('Player choice:', user_choice)
    print('Computer choice:', computer_choice)
    return user_choice, computer_choice

def check_rules(user_choice, computer_choice, player_wins, computer_wins):
    if user_choice == computer_choice:
        print('Tie')
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print('Scissors are destroyed by rock')
            print('Player wins')
            player_wins += 1
        else:
            print('Paper covers rock')
            print('Computer wins')
            computer_wins += 1
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('Paper covers rock')
            print('Player wins')
            player_wins += 1
        else:
            print('Scissors cut paper')
            print('Computer wins')
            computer_wins += 1
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print('Scissors cut paper')
            print('Player wins')
            player_wins += 1
        else:
            print('Rock destroys scissors')
            print('Computer wins')
            computer_wins += 1
    
    return player_wins, computer_wins

def check_winner(player_wins, computer_wins):
    if computer_wins == 2:
        print('Computer wins the game')
        exit()

    if player_wins == 2:
        print('Player wins the game')
        exit()

def run_game():
    player_wins = 0
    computer_wins = 0
    rounds = 1

    while True:
        print('*' * 10)
        print('Round', rounds)
        print('*' * 10)

        print('Computer wins:', computer_wins)
        print('Player wins:', player_wins)

        rounds += 1

        user_choice, computer_choice = choose_options()

        player_wins, computer_wins = check_rules(user_choice, computer_choice, player_wins, computer_wins)

        check_winner(player_wins, computer_wins)
            
run_game()