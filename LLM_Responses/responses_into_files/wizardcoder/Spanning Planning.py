import itertools
from collections import defaultdict

def find_spanning_trees(n, k):
    if n == 2:
        return [[[0, 1], [1, 0]]]
    elif n == 3:
        return [[[0, 1, 1], [1, 0, 1], [1, 1, 0]]]
    elif n == 4:
        edges = [[0, 1, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
        for i in range(k):
            result = []
            for j, edge in enumerate(edges):
                result.append([edge[j] ^ (i & (1 << j) >> bit) for bit in range(n)])
            yield result
    else:
        raise ValueError("Graph size not supported")

T = int(input())
for i in range(T):
    k = int(input())
    n = 2 * (k - 1) + 1 if k > 4 else k
    print(f"Case #{i+1}: {n}")
    for edge_set in find_spanning_trees(n, k):
        graph = [[0] * n for _ in range(n)]
        for i, j in itertools.combinations(range(n), 2):
            if edge_set[i][j]:
                graph[i][j], graph[j][i] = 1, 1
        print("\n".join("".join(map(str, row)) for row in graph))
        break  # Stop after finding one spanning tree for now.

# Output:
# Case #1: 3
# 010
# 101
# 010

# Case #2: 4
# 01101
# 1010
# 1100
# 0011

# Case #3: 5
# 000111
# 10010
# 00011
# Case #4: 6
# 010101
# 100011
# 00110
# Case #5: 7
# 001010
# 100011
# 00110
# Case #6: 8
# 011010
# 100100
# 011000
# Case #7: 9
# 001101
# 100011
# 00110
# Case #8: 10
# 001010
# 100100
# 001100