
# Tic-Tac-Toe Game

board = [" "] * 9
current_player = "X"

def display_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()

def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

print("Welcome to Tic-Tac-Toe!")
print("Choose a position from 1 to 9:")

while True:
    display_board()

    try:
        position = int(input(
            "Player " + current_player + ", enter position (1-9): "
        ))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue

    if position < 1 or position > 9:
        print("Choose a position between 1 and 9.")
        continue

    if board[position - 1] != " ":
        print("That position is already occupied. Try again.")
        continue

    board[position - 1] = current_player

    winner = check_winner()

    if winner:
        display_board()
        print("Player", winner, "wins!")
        break

    if " " not in board:
        display_board()
        print("It's a draw!")
        break

    # Switch player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
