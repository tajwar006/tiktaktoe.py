def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def main():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Variable to keep track of the current player ('X' or 'O')
    current_player = 'X'

    while True:
        print_board(board)

        # Get the user input for the move
        row = int(input(f"Enter the row (0, 1, 2) for {current_player}: "))
        col = int(input(f"Enter the column (0, 1, 2) for {current_player}: "))

        # Check if the cell is empty
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell is already occupied. Try again.")
            continue

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("The game ends in a draw!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
