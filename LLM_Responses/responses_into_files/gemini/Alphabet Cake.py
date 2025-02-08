def solve():
    R, C = map(int, input().split())
    cake = [list(input()) for _ in range(R)]

    initials = {}
    for r in range(R):
        for c in range(C):
            if cake[r][c] != '?':
                initials[cake[r][c]] = (r, c)

    for initial, (r, c) in initials.items():
        for i in range(R):
            for j in range(C):
                if cake[i][j] == '?':
                    if i >= r and i <= r and j >=c and j <=c:
                        cake[i][j] = initial
                    elif i >= min(r, i) and i <= max(r, i) and j >= min(c, j) and j <= max(c, j):
                        cake[i][j] = initial

    
    for r in range(R):
        for c in range(C):
            if cake[r][c] == '?':
                found = False
                for init in initials:
                    if found == False:
                        cake[r][c] = init
                        found = True


    for row in cake:
        print("".join(row))


T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}:")
    solve()