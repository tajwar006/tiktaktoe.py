board = [[" "," "," "],
		 [" "," "," "],
		 [" "," "," "]]
def printBoard(board):
    for row in board:
        print("|".join(row))
       

def Drawn(board):
    for row in board:
        for place in row:
            if place == ' ':
                return False
    return True

def Winner(board, player):
    for row in board:
        if all(place == player for place in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        printBoard(board)

        row = int(input("Enter the row (0, 1, 2) for current player: "))
        col = int(input("Enter the column (0, 1, 2) for current player: "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("This place is taken. Try again.")
            continue

        if Winner(board, current_player):
            PrintBoard(board)
            print("Player {current_player} wins!")
            break

        if Drawn(board):
            PrintBoard(board)
            print("The game is a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
start = str(input("would you like to play tiktaktoe?  "))
if start == "yes":
    main()
elif start == "no":
	print("bye")
