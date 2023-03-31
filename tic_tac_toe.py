delimiter = 44* "="
print(f"Welcome to Tic Tac Toe\n{delimiter}\n\
GAME RULES:\n\
Each player can place one mark (or stone)\n\
per turn on the 3x3 grid. The WINNER is\n\
who succeeds in placing three of their\n\
marks in a:\n\
* horizontal,\n\
* vertical or\n\
* diagonal row\n{delimiter}\n\
Let's start the game")
print(44 *"-")	

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def create_board() -> str:
    """Returns a string representation of the board."""
    return (
f"+---+---+---+\n\
| {board[0]} | {board[1]} | {board[2]} |\n\
+---+---+---+\n\
| {board[3]} | {board[4]} | {board[5]} |\n\
+---+---+---+\n\
| {board[6]} | {board[7]} | {board[8]} |\n\
+---+---+---+"
)


print(create_board())
turn = "O" 

while True:
    print(delimiter)
    guess = input(f"Player {turn} | Enter your move number (1-9): ")
    print(delimiter)
    if guess.isdigit():
        index = int(guess) - 1
        if 0 <= index <= 8 and board[index] == " ":
            board[index] = board[index].replace(" ", turn)
            print(create_board())
            if (board[0] == board[1] == board[2] != " ") or \
                (board[3] == board[4] == board[5] != " ") or \
                (board[6] == board[7] == board[8] != " ") or \
                (board[0] == board[3] == board[6] != " ") or \
                (board[1] == board[4] == board[7] != " ") or \
                (board[2] == board[5] == board[8] != " ") or \
                (board[0] == board[4] == board[8] != " ") or \
                (board[2] == board[4] == board[6] != " "):
                print(f"{delimiter}\n\
Congratulations, the player {turn} WON!\n{delimiter}")
                break
            elif " " not in board:
                print(f"{delimiter}\n\
The game is a tie!\n{delimiter}")
                break
            if turn == "O":
                turn = "X"
            else:
                turn = "O"
        else:
            print("Invalid move, please try again.")
    else:
        print("Invalid input, please enter a number (1-9).")
