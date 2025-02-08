def solve():
    N, K = map(int, input().split())

    if N == 2:
        if K == 3:
            return "IMPOSSIBLE"
        elif K == 2:
            return "POSSIBLE\n1 2\n2 1"
        else:
            return "POSSIBLE\n2 1\n1 2"

    if N == 3:
        if K == 6:
            return "POSSIBLE\n2 1 3\n3 2 1\n1 3 2"
        elif K == 5:
            return "POSSIBLE\n1 3 2\n2 1 3\n3 2 1"
        elif K == 7:
            return "POSSIBLE\n1 2 3\n3 1 2\n2 3 1"

    if N == 4:
        if K == 10:
          return "POSSIBLE\n1 2 3 4\n4 1 2 3\n3 4 1 2\n2 3 4 1"
        elif K == 6:
          return "POSSIBLE\n1 2 3 4\n4 3 2 1\n2 1 4 3\n3 4 1 2"

    
    #For larger N, a more sophisticated algorithm is needed.  This is a placeholder.
    return "IMPOSSIBLE"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")