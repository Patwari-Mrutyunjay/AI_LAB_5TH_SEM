
def depth_limited_search(graph, node, goal, limit, path):
    # Check whether the goal is reached
    if node == goal:
        return path

    # Stop if the depth limit is reached
    if limit == 0:
        return None

    # Explore each child
    for child in graph.get(node, []):
        # Avoid revisiting a node already on this path
        if child not in path:
            result = depth_limited_search(
                graph, child, goal, limit - 1,
                path + [child]
            )

            if result is not None:
                return result

    return None


def iterative_deepening_search(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print("Depth limit:", depth)

        result = depth_limited_search(
            graph, start, goal, depth, [start]
        )

        if result is not None:
            print("Goal found!")
            print("Solution path:", " -> ".join(result))
            return result

        print("Goal not found. Increasing depth limit.\n")

    print("Goal not found within the depth limit.")
    return None


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = 'A'
goal = 'F'

iterative_deepening_search(
    graph, start, goal, max_depth=5
)
