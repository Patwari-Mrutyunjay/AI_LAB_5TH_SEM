
import heapq

def manhattan(state, goal):
    distance = 0

    for i, tile in enumerate(state):
        if tile == 0:
            continue

        current_row, current_col = divmod(i, 3)
        goal_index = goal.index(tile)
        goal_row, goal_col = divmod(goal_index, 3)

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    neighbors = []

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col

            board = list(state)
            board[blank], board[new_index] = (
                board[new_index], board[blank]
            )

            neighbors.append(tuple(board))

    return neighbors


def a_star(start, goal):
    open_list = []
    counter = 0

    g_score = {start: 0}
    parent = {start: None}

    heapq.heappush(
        open_list,
        (manhattan(start, goal), counter, start)
    )

    while open_list:
        f, _, current = heapq.heappop(open_list)

        # Ignore outdated queue entries
        if f != g_score[current] + manhattan(current, goal):
            continue

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for child in get_neighbors(current):
            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(child, float("inf")):
                g_score[child] = tentative_g
                parent[child] = current

                counter += 1
                h = manhattan(child, goal)
                f = tentative_g + h

                heapq.heappush(
                    open_list, (f, counter, child)
                )

    return None


def display(board):
    for i in range(0, 9, 3):
        print(*board[i:i + 3])
    print()


start = (1, 2, 3,
         5, 0, 6,
         4, 7, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

path = a_star(start, goal)

if path:
    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for step, state in enumerate(path):
        print("Step", step)
        display(state)
else:
    print("No solution found.")
