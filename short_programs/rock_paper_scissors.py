import sys
import random
print('ROCK PAPER SCISSOR GAME')
wins=0
loses=0
ties=0

while True:
    print('%s wins,%s loses,%s ties',(wins,loses,ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input('>')
        if player_move == 'q':
                sys.exit()  # Quit the program.
        if player_move == 'r' or player_move == 'p' or player_move == 's':
                break  # Break out of the player input loop.
        print('Type one of r, p, s, or q.')
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')
    move_number = random.randint(1, 3)
    if move_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        loses = loses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        loses = loses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        loses = loses + 1



