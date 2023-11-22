
# Online Python - IDE, Editor, Compiler, Interpreter

board = [[" "," "," "],
		 [" "," "," "],
		 [" "," "," "]]
def printBoard(board):
    for row in board:
        print("|".join(row))


def checkforerror(board):
    for row in board:
        for place in row:
            if place == ' ':
                return False
        else:
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
def turns():
    currentplayer = 'X'

    while True:
        printBoard(board)

        row = int(input("Enter the row (0, 1, 2) for current player : "))
        col = int(input("Enter the column (0, 1, 2) for current player : "))
        
        


        if board[row][col] == ' ':
            board[row][col] = currentplayer
        else:
            print("This place is taken. Try again.")
            continue

        if Winner(board, currentplayer):
            PrintBoard(board)
            print("Player",currentplayer, "wins!")
            break

        if checkforerror(board):
            PrintBoard(board)
            print("The game is a draw!")
            break
        if currentplayer == "X":
            currentplayer = "O"
        else:
            currentplayer == "X"
start = str(input("would you like to play tiktaktoe?  "))
if start == "yes":
    turns()
else:
	print("bye")