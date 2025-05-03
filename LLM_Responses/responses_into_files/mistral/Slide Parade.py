import sys
from collections import defaultdict
input = sys.stdin.readline

def solve(B, S):
    graph = defaultdict(list)
    for _ in range(S):
        u, v = map(int, input().split())
        graph[u].append(v)

    visited = set([1])
    queue = [(1, 1)]
    steps = 0

    while queue:
        b, s = queue.pop(0)
        for next_b in graph[b]:
            if next_b not in visited:
                visited.add(next_b)
                queue.append((next_b, s+1))
                steps += 1

    if len(visited) != B:
        return "IMPOSSIBLE"

    route = [1] + list(visited) * (steps - 1) + [1]
    return f'Case #{T+1}: {len(route)}' + '\n' + ' '.join(str(x) for x in route)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        B, S = map(int, input().split())
        print(solve(B, S))