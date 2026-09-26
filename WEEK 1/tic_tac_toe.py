import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        row = [str(i * 3 + j + 1) if board[i * 3 + j] == " " else board[i * 3 + j] for j in range(3)]
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("---+---+---")
    print()

def check_win(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(b[idx] == player for idx in cond) for cond in win_conditions)

def check_draw(b):
    return " " not in b

def minimax(b, depth, is_maximizing):
    if check_win(b, "O"):
        return 1
    if check_win(b, "X"):
        return -1
    if check_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

def get_ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def play_game():
    print("Welcome to Tic-Tac-Toe AI!")
    print("You are 'X' and the Computer AI is 'O'.")

    current_player = "X"

    while True:
        print_board()

        if current_player == "X":
            try:
                choice = int(input("Choose an empty slot (1-9): ")) - 1
                if choice < 0 or choice > 8 or board[choice] != " ":
                    print("Invalid move! Pick an empty slot from 1 to 9.")
                    continue
                board[choice] = "X"
            except ValueError:
                print("Please enter a valid number from 1 to 9.")
                continue
        else:
            print("AI is thinking...")
            move = get_ai_move()
            if move is not None:
                board[move] = "O"
                print(f"AI chose slot {move + 1}")

        if check_win(board, current_player):
            print_board()
            if current_player == "X":
                print("Congratulations! You won!")
            else:
                print("AI wins! Better luck next time.")
            break

        if check_draw(board):
            print_board()
            print("It's a perfect tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()