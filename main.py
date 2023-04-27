from helpers import draw_board, check_turn, check_for_win
import os

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    # Reset screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    # Let player know for invalid input
    if prev_turn == turn:
        print('Invalid spot selected, please pick another.')
    prev_turn = turn
    print("Player " + str((turn%2)+1) + "'s turn: Pick your spot or press q to quit:")
    # Get input from player
    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        # Check if spot is already blocked
        if not spots[int(choice)] in {"X", "O"}:
            # Valid input, update board
            turn += 1
            spots[int(choice)] = check_turn(turn)
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False

# Draw the board one last time
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
# If there is a winner, let us know
if complete:
    if check_turn(turn) == 'X': print("Player 1 wins.")
    else: print('Player 2 wins.')
else:
    print("No winner")

print("Thanks for playing.")