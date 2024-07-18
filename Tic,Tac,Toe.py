def print_board(board):
    """
    Function to print the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """
    Function to check if there's a winner.
    Returns 'X' if player X wins, 'O' if player O wins, or None if no winner yet.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    """
    Function to check if the board is full.
    Returns True if the board is full, False otherwise.
    """
    for row in board:
        if ' ' in row:
            return False
    return True

def is_valid_move(board, row, col):
    """
    Function to check if a move is valid.
    Returns True if the move is valid (within bounds and the cell is empty), False otherwise.
    """
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != ' ':
        return False
    return True

def get_player_move(player, board):
    """
    Function to get the player's move.
    """
    while True:
        try:
            print(f"Player {player}, enter your move (row column): ")
            move = input().strip()
            row, col = map(int, move.split())
            if is_valid_move(board, row, col):
                return row, col
            else:
                print("Invalid move! Please try again.")
        except ValueError:
            print("Invalid input! Please enter two integers separated by space.")

def play_tic_tac_toe():
    """
    Function to play Tic Tac Toe game.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        row, col = get_player_move(player, board)
        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_tic_tac_toe()
    else:
        print("Thanks for playing!")

# Start the game
play_tic_tac_toe()
