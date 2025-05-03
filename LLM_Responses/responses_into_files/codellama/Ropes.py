import sys

def solve(T, N, W):
    # Initialize variables
    score = 0
    ropes = []
    for i in range(N):
        ropes.append([])

    # Play the game
    for t in range(T):
        for i in range(N):
            A, B = map(int, input().split())
            C, D = map(int, input().split())
            if (A, B) not in ropes[i] and (C, D) not in ropes[i]:
                score += 1
                ropes[i].append((A, B))
                ropes[i].append((C, D))

    # Print the result
    if score >= W:
        print(1)
    else:
        print(0)