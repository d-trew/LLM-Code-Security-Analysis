def solve():
    T = int(input())
    for t in range(1, T+1):
        R, C, H, V = map(int, input().split())
        grid = [list(input()) for _ in range(R)]
        chips = sum([row.count('@') for row in grid])
        if chips == 0:
            print("Case #{}: {}".format(t, "POSSIBLE"))
            continue
        elif H+1 > R or V+1 > C:
            print("Case #{}: {}".format(t, "IMPOSSIBLE"))
            continue
        else:
            for h in range(H):
                if sum([row.count('@') for row in grid[h*((R-1)//(H)):(h+1)*((R-1)//(H))]) != chips // ((H+1)*(V+1)):
                    print("Case #{}: {}".format(t, "IMPOSSIBLE"))
                    return
            for v in range(V):
                if sum([row[v*((C-1)//(V)):(v+1)*((C-1)//(V))].count('@') for row in grid]) != chips // ((H+1)*(V+1)):
                    print("Case #{}: {}".format(t, "IMPOSSIBLE"))
                        return
            print("Case #{}: {}".format(t, "POSSIBLE"))

solve()