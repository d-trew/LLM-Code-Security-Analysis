def solve(R, C, S_row, S_col):
    if sum(S_row) != R * max(S_row) or sum(S_col) != C * max(S_col):
        return "IMPOSSIBLE"
    
    matrix = [['/' if i < j and (i + j) % 2 == 0 else '\\' for j in range(C)] for i in range(R)]
    
    for i in range(min(R, C)):
        if S_row[i] > 0:
            matrix[i][0] = '/'
            S_row[i] -= 1
        if S_col[i] > 0:
            matrix[0][i] = '\\'
            S_col[i] -= 1
    
    for i in range(min(R, C)):
        for j in range(S_row[i]):
            if (j + i) % 2 == 0:
                matrix[i][j + 1] = '/'
            else:
                matrix[i][j + 1] = '\\'
    
    for i in range(min(R, C)):
        for j in range(S_col[i]):
            if (j + i) % 2 == 0:
                matrix[j + 1][i] = '/'
            else:
                matrix[j + 1][i] = '\\'
    
    return "POSSIBLE\n" + "\n".join("".join(row) for row in matrix)

T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    S_row = list(map(int, input().split()))
    S_col = list(map(int, input().split()))
    
    print("Case #{}: {}".format(tc, solve(R, C, S_row, S_col)))