# Tic-Tac-Toe

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('---'*len(row))

def player_move(board, player):
    while True:
        try:
            row = int(input(f"{player} Enter a row to move:(0-2: ) "))
            col = int(input(f"{player} Enter a column to move:(0-2: ) "))
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("That already has a space.")
        except (IndexError, ValueError):
            print("Invalid input. Please enter numbers between 0 and 2.")

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def switch_player(player):
    return 'O' if player == 'X' else 'X'

def main():
    board = initialize_board()
    current_player = "X"

    while True:
        display_board(board)
        player_move(board, current_player)

        if check_win(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = switch_player(current_player)

if __name__ == '__main__':
    main()

