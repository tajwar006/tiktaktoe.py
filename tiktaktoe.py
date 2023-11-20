def printBoard(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def Drawn(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def Winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
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

        row = int(input(f"Enter the row (0, 1, 2) for {current_player}: "))
        col = int(input(f"Enter the column (0, 1, 2) for {current_player}: "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("This place is taken. Try again.")
            continue

        if Winner(board, current_player):
            PrintBoard(board)
            print(f"Player {current_player} wins!")
            break

        if Drawn(board):
            PrintBoard(board)
            print("The game is a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
