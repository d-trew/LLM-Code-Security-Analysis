def solve(c, j):
    c = list(c)
    j = list(j)
    
    for i in range(len(c)):
        if c[i] == '?' and j[i] != '?':
            c[i] = str((int(j[i]) + 10 - int(c[i-1])) % 10)
        elif j[i] == '?' and c[i] != '?':
            j[i] = str((int(c[i]) + 10 - int(j[i-1])) % 10)
    
    for i in range(len(c)-1, -1, -1):
        if c[i] == '?' and j[i] != '?':
            c[i] = str((int(j[i]) + 10 - int(c[(i+1)%len(c)])) % 10)
        elif j[i] == '?' and c[i] != '?':
            j[i] = str((int(c[i]) + 10 - int(j[(i+1)%len(j)])) % 10)
    
    return "".join(c), "".join(j)

T = int(input())
for t in range(T):
    C, J = input().split()
    c, j = solve(C, J)
    print("Case #{}: {}, {}".format(t+1, c, j))