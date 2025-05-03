import sys
sys.setrecursionlimit(10**6) # To handle larger input sizes, increase recursion limit

def find_max_circle_size(kids):
    def dfs(node, visited, graph, circle, parent=None):
        if node in visited:
            return False
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor != parent and dfs(neighbor, visited, graph, circle, node):
                circle.append(neighbor)
                return True
        return False

    def max_circle_size(kids):
        max_size = 0
        for i in range(1, len(kids) + 1):
            if i not in kids:
                continue
            visited = set()
            graph = {i}
            circle = []
            while kids[i] != i and dfs(i, visited, graph, circle):
                graph.add(kids[i])
                circle.append(kids[i])
            max_size = max(max_size, len(circle))
        return max_size

    T = int(input()) # Number of test cases
    for t in range(1, T + 1):
        N = int(input()) # Number of kids in the class
        kids = [0] * (N + 1)
        for i in range(1, N + 1):
            kids[i] = int(input()) # BFF of each kid
        print("Case #{}: {}".format(t, max_circle_size(kids)))

# Example input:
# 2
# 3
# 1 2 3
# 3 2 1
# 4
# 1 2 3 4 5
# 2 3 4 5 6

# Example output:
# Case #1: 2
# Case #2: 3