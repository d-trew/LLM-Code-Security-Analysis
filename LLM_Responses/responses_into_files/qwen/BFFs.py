def max_bff_circle(N, F):
    graph = [[] for _ in range(N)]
    for i in range(N):
        graph[i].append(F[i] - 1)
        graph[F[i] - 1].append(i)

    visited = [False] * N
    def dfs(node, parent):
        if visited[node]:
            return 0
        visited[node] = True
        size = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                size += dfs(neighbor, node)
        return size

    max_circle_size = 0
    for i in range(N):
        if not visited[i]:
            circle_size = dfs(i, -1)
            if circle_size % 2 == 0:
                max_circle_size = max(max_circle_size, circle_size)

    return max_circle_size

def solve():
    T = int(input())
    results = []
    for t in range(1, T + 1):
        N = int(input())
        F = list(map(int, input().split()))
        result = max_bff_circle(N, F)
        results.append(f"Case #{t}: {result}")

    for result in results:
        print(result)

if __name__ == "__main__":
    solve()