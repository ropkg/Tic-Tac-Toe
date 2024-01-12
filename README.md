# Tic-Tac-Toe Game

Welcome to the classic Tic-Tac-Toe game where you can play against a computer opponent. The game is played on a 3x3 grid, and the first one to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.

## Features

- **Player vs. Computer:** Play against a computer opponent that uses the minimax algorithm for intelligent moves.
- **Interactive Console Interface:** The game has an interactive console interface, allowing the player to input moves.
- **Winning Conditions:** The game checks for winning conditions and declares a winner when applicable.
- **Tie Game:** If the board is filled and no player has won, the game declares a tie.

## How to Play

1. Run the script in a Python environment.
2. Enter your move when prompted (1-9) during your turn.
3. The computer will make its move, and the board will be updated.
4. Continue taking turns until a winner is declared or the game ends in a tie.

## Code Structure

- `print_board(board)`: Function to print the current state of the Tic-Tac-Toe board.
- `check_winner(board, player)`: Function to check if a player has won.
- `is_board_full(board)`: Function to check if the board is full, resulting in a tie.
- `get_player_move(board)`: Function to get the player's move input.
- `get_computer_move(board, computer_mark, player_mark)`: Function to get the computer's move using the minimax algorithm.
- `play_tic_tac_toe()`: Main function to run the Tic-Tac-Toe game loop.

## Future Enhancements

- **Graphical User Interface (GUI):** Develop a graphical user interface for a more user-friendly experience.
- **Scalability:** Allow users to choose the board size and winning conditions for a more customizable game.

## Contributors

- Rohit Muthukumarasamy

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute and enjoy playing Tic-Tac-Toe!

