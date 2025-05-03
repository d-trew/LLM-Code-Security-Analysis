from collections import defaultdict

def bfs_shortest_path(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            for next_vertex in graph[vertex]:
                if next_vertex == goal:
                    return path + [next_vertex]
                else:
                    queue.append((next_vertex, path + [next_vertex]))
            visited.add(vertex)
    return None

def catch_alice(J, C, A, Q, corridors):
    graph = defaultdict(list)
    for u, v in corridors:
        graph[u].append(v)
        graph[v].append(u)

    # Alice's optimal first move
    alice_moves = [None] * J
    for i in range(1, J + 1):
        if i != A and i != Q:
            path = bfs_shortest_path(graph, A, i)
            if path:
                alice_moves[i] = len(path)

    min_moves = float('inf')
    best_move = None

    # Find the move that minimizes the number of moves to catch Alice
    for u in range(1, J + 1):
        if u != A and u != Q:
            path = bfs_shortest_path(graph, Q, u)
            if path:
                queen_moves = len(path)
                if alice_moves[u] is not None:
                    total_moves = queen_moves + alice_moves[u]
                    if total_moves < min_moves:
                        min_moves = total_moves
                        best_move = u

    # If Alice cannot be caught in 10^9 moves, return "SAFE"
    if min_moves > 10**9:
        return "SAFE"

    return min_moves

# Read input and process each test case
import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])
index = 1
results = []

for _ in range(T):
    J = int(data[index])
    C = int(data[index + 1])
    A = int(data[index + 2])
    Q = int(data[index + 3])
    index += 4

    corridors = []
    for _ in range(C):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        corridors.append((u, v))

    result = catch_alice(J, C, A, Q, corridors)
    results.append(result)

# Output the results
for i, result in enumerate(results):
    print(f"Case #{i+1}: {result}")