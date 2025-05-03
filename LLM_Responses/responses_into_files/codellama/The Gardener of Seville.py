T = int(input())
for t in range(1, T + 1):
    R, C = map(int, input().split())
    courtiers = list(map(int, input().split()))
    graph = {}
    for i in range(len(courtiers)):
        pair = tuple(sorted([courtiers[i], courtiers[(i+1)%len(courtiers)]]))
        if pair not in graph:
            graph[pair] = []
        graph[pair].append((R-1, C-1))
    visited = set()
    def dfs(x, y):
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in visited:
                for pair, paths in graph.items():
                    if (nx, ny) in paths:
                        for px, py in paths:
                            if dfs(px, py):
                                return True
                visited.add((nx, ny))
                return False
        return True

    result = "IMPOSSIBLE"
    for r in range(R):
        for c in range(C):
            if (r, c) not in visited and dfs(r, c):
                result = ""
                for row in range(R):
                    for col in range(C):
                        if (row, col) == (0, 0): 
                            print("Case #{}:".format(t), end="")
                        elif row == R - 1:
                            if col == C - 1: 
                                print("/")
                            else: 
                                print("\\")
                        else:
                            if col == C - 1: 
                                print("/")
                            else: 
                                print("\\")
                break
    if result == "IMPOSSIBLE":
        print(result)