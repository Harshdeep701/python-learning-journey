import random
# write code for tic tac toe game in python
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)      
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

    def get_empty_positions(board):
        # Initialize an empty list to store available positions
        positions = []
        # Iterate through all rows and columns of the board
        for i in range(3):
            for j in range(3):
                # Check if the position is empty (contains a space)
                if board[i][j] == " ":
                    # Add the empty position as a tuple (row, col) to the list
                    positions.append((i, j))
        # Return the list of all empty positions on the board
        return positions

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter col (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Position already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def computer_move(board):
    positions = get_empty_positions(board)
    if positions:
        row, col = random.choice(positions)
        board[row][col] = "O"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("You win!")
            break
        if not get_empty_positions(board):
            print("It's a draw!")
            break
        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("Computer wins!")
            break
        if not get_empty_positions(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main() 