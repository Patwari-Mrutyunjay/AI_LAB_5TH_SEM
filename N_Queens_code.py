def heuristic(board):
    conflicts = 0

    for c1 in range(8):
        for c2 in range(c1 + 1, 8):
            r1 = board[c1]
            r2 = board[c2]

            # Same row or same diagonal
            if r1 == r2 or abs(r1 - r2) == abs(c1 - c2):
                conflicts += 1

    return conflicts


def print_board(board):
    for row in range(1, 9):
        for col in range(8):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Same example boards from the trace
steps = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 5, 1, 1, 1, 1, 1, 1],
    [1, 5, 8, 1, 1, 1, 1, 1],
    [1, 5, 8, 6, 1, 1, 1, 1],
    [1, 5, 8, 6, 3, 1, 1, 1],
    [1, 5, 8, 6, 3, 7, 1, 1],
    [1, 5, 8, 6, 3, 7, 2, 1],
    [1, 5, 8, 6, 3, 7, 2, 4]
]

for i, board in enumerate(steps):
    print(f"\nStep {i}: {board}")
    print("Heuristic:", heuristic(board))
    print_board(board)

print("\nSolution found!")
