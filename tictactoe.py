import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(available_moves)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_mark = "X"
    computer_mark = "O"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's turn
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = player_mark
        print_board(board)

        if check_winner(board, player_mark):
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        # Computer's turn
        print("Computer's turn:")
        computer_row, computer_col = get_computer_move(board)
        board[computer_row][computer_col] = computer_mark
        print_board(board)

        if check_winner(board, computer_mark):
            print("Computer wins! Better luck next time.")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
