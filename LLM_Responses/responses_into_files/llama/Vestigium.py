T = int(input())
for _ in range(T):
    N = int(input())
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    trace = sum(matrix[i][i] for i in range(N))
    repeated_rows = set()
    repeated_cols = set()
    for i in range(N):
        row_set = set(matrix[i])
        col_set = set(x[i] for x in matrix)
        if len(row_set) != N:
            repeated_rows.add(i+1)
        if len(col_set) != N:
            repeated_cols.add(i+1)
    
    print(f"Case #{_+1}: {trace} {(len(repeated_rows))} {(len(repeated_cols))}")