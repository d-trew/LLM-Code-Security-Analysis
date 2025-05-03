T = int(input())
for _ in range(T):
    J, C, A, Q = map(int, input().split())
    graph = {}
    for i in range(C):
        U, V = map(int, input().split())
        if U not in graph:
            graph[U] = []
        if V not in graph:
            graph[V] = []
        graph[U].append(V)
        graph[V].append(U)
    min_moves = 0
    for _ in range(10**9):
        moves = 0
        a_pos, q_pos = A, Q
        while True:
            if a_pos == q_pos:
                print(f"Case #{_+1}: CATCH")
                exit()
            moves += 2
            q_move = min((x for x in graph[q_pos] if x != a_pos), default=None)
            if q_move is None:
                print(f"Case #{_+1}: SAFE")
                exit()
            a_pos, q_pos = q_move, q_pos
    print(f"Case #{_+1}: {min_moves}")