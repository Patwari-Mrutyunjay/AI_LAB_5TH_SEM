
import random
import math


def manhattan(state, goal):
    distance = 0

    for i, tile in enumerate(state):
        if tile == 0:
            continue

        current_row, current_col = divmod(i, 3)
        goal_index = goal.index(tile)
        goal_row, goal_col = divmod(goal_index, 3)

        distance += (
            abs(current_row - goal_row)
            + abs(current_col - goal_col)
        )

    return distance


def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col

            new_state = list(state)
            new_state[blank], new_state[new_index] = (
                new_state[new_index], new_state[blank]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def simulated_annealing(
    start, goal, temperature=10,
    cooling_rate=0.995, max_steps=10000
):
    current = tuple(start)
    goal = tuple(goal)
    path = [current]

    for step in range(max_steps):
        if current == goal:
            print("Goal reached!")
            print("Moves:", len(path) - 1)

            for state in path:
                for i in range(0, 9, 3):
                    print(state[i:i + 3])
                print()

            return path

        if temperature < 0.001:
            break

        neighbor = random.choice(get_neighbors(current))

        current_cost = manhattan(current, goal)
        new_cost = manhattan(neighbor, goal)
        delta = new_cost - current_cost

        # Accept better states, sometimes accept worse states
        if delta <= 0 or random.random() < math.exp(
            -delta / temperature
        ):
            current = neighbor
            path.append(current)

        # Cool down
        temperature *= cooling_rate

    print("Goal not reached within the search limit.")
    return None


start = (
    1, 2, 3,
    4, 5, 6,
    7, 0, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

simulated_annealing(start, goal)
