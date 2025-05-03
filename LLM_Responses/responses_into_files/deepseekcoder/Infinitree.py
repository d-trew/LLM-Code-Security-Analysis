from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def solve():
    N, A, B = map(int, input().split())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    
    G = defaultdict(list)
    for i in range(N):
        if L[i] != 0:
            G[L[i], 1].append((i+2, 2))
            G[(i+2, 2)].append((L[i], 1))
        if R[i] != 0:
            G[R[i], 2].append((i+2, 3))
            G[(i+2, 3)].append((R[i], 2))
    
    def bfs(start):
        visited = [False]*(N+1)
        q = deque([(start, 0)])
        while q:
            node, d = q.popleft()
            if node == B: return d
            for nxt_node, _ in G[node]:
                if not visited[nxt_node]:
                    visited[nxt_node] = True
                    q.append((nxt_node, d+1))
        return -1
    
    print(bfs((1, 1)))

T = int(input())
for t in range(1, T+1):
    solve()