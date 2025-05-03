T = int(input())
for _ in range(T):
    N = int(input())
    tree_edges = []
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree_edges.append((a, b))
    
    M = int(input())
    for _ in range(M):
        K = int(input())
        A = list(map(int, input().split()))
        Vreni_move = [K]
        for i in range(K - 1):
            Vreni_move.append(A[i])
        print(*Vreni_move)