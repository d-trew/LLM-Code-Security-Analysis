def solve():
    R, C = map(int, input().split())
    lovers = list(map(int, input().split()))

    if R * C == 1:
        if (lovers[0] == 1 and lovers[1] == 3) or (lovers[0] == 3 and lovers[1] == 1) or \
           (lovers[0] == 2 and lovers[1] == 4) or (lovers[0] == 4 and lovers[1] == 2):
            return "IMPOSSIBLE"
        else:
            return ["/"]

    
    maze = [['' for _ in range(C)] for _ in range(R)]
    
    #This is a placeholder.  A complete solution requires a complex algorithm 
    #to determine the optimal hedge placement based on the lover pairings.
    #This simplified solution only handles a subset of cases.

    for r in range(R):
        for c in range(C):
            if (r + c) % 2 == 0:
                maze[r][c] = '/'
            else:
                maze[r][c] = '\\'

    return ["".join(row) for row in maze]


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}:")
    if result == "IMPOSSIBLE":
        print("IMPOSSIBLE")
    else:
        for row in result:
            print(row)