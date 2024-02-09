import random
import os.path
import json

random.seed()


def draw_board(board):
    # Develop code to draw the board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def welcome(board):
    # Prints the welcome message
    print("Welcome to Noughts and Crosses!\n")
    # Displays the board by calling draw_board(board)
    draw_board(board)


def initialise_board(board):
    # Develop code to set all elements of the board to one space ' '
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board


def get_player_move(board):
    # Develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cell already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")


def choose_computer_move(board):
    # Develop code to let the computer choose a cell to put a nought in
    # and return row and col
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col


def check_for_win(board, mark):
    # Develop code to check if either the player or the computer has won
    # Return True if someone won, False otherwise
    for i in range(3):
        # Check rows and columns
        if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False


def check_for_draw(board):
    # Develop code to check if all cells are occupied
    # Return True if it is, False otherwise
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def play_game(board):
    # Develop code to play the game
    # Start with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    board = initialise_board(board)

    # Then draw the board
    draw_board(board)

    while True:
        # Get the player move
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = 'X'
        draw_board(board)

        # Check if the player has won
        if check_for_win(board, 'X'):
            return 1  # Player won

        # Check for a draw
        if check_for_draw(board):
            return 0  # Draw

        # Choose a move for the computer
        comp_row, comp_col = choose_computer_move(board)
        board[comp_row][comp_col] = 'O'
        draw_board(board)

        # Check if the computer has won
        if check_for_win(board, 'O'):
            return -1  # Computer won

        # Check for a draw
        if check_for_draw(board):
            return 0  # Draw


def menu():
        """Displays the menu and manages user choices.
           Options:
           1. Play game
           2. Save score to 'leaderboard.txt'
           3. Load and show scores from 'leaderboard.txt'
           q. Quit
           Returns:
           None """
        # Get user input
        while True:
            print("1 - Play the game")
            print("2 - Save score in file 'leaderboard.txt'")
            print("3 - Load and display the scores from the 'leaderboard.txt'")
            print("q - End the program")
            choice = input("Enter your choice: ").lower()
            if choice in ['1', '2', '3', 'q']:
                return choice
            else:
                print("Invalid choice! Please enter '1', '2', '3', or 'q'.")


def load_scores():
    # Develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # Return the scores in a Python dictionary
    # with the player names as keys and the scores as values
    try:
        with open('leaderboard.txt', 'r') as file:
            leaders = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file is not found or can't be decoded, return an empty dictionary
        leaders = {}
    return leaders


def save_score(score):
    # Develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    player_name = input("Enter your name: ")
    leaders = load_scores()

    # Update the leaderboard with the new score
    leaders[player_name] = score

    with open('leaderboard.txt', 'w') as file:
        # Save the updated leaderboard to the file
        json.dump(leaders, file)


def display_leaderboard(leaders):
    # Develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    print("Leaderboard:")
    for name, score in leaders.items():
        print(f"{name}: {score}")
