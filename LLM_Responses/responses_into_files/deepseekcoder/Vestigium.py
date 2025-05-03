def solve(matrix):
    n = len(matrix)
    trace = 0
    row_counts = [0]*n
    col_counts = [0]*n
    
    for i in range(n):
        values = set()
        for j in range(n):
            if matrix[i][j] in values:
                row_counts[i] = 1
            else:
                values.add(matrix[i][j])
                
            if i == j:
                trace += matrix[i][j]
    
    for j in range(n):
        values = set()
        for i in range(n):
            if matrix[i][j] in values:
                col_counts[j] = 1
            else:
                values.add(matrix[i][j])
    
    return sum(row_counts), sum(col_counts), trace

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    r, c, t = solve(matrix)
    print(f"Case #{tc}: {t} {r} {c}")