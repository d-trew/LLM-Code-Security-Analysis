def solve():
    R, C = map(int, input().split())
    rows = list(map(int, input().split()))
    cols = list(map(int, input().split()))

    def is_square_free(matrix):
        for r1 in range(R):
            for c1 in range(C):
                if matrix[r1][c1] == '/':
                    for r2 in range(r1 + 1, R):
                        for c2 in range(c1 + 1, C):
                            if matrix[r1][c2] == '\\' and \
                               matrix[r2][c1] == '\\' and \
                               matrix[r2][c2] == '/':
                                return False
                            if matrix[r1][c2] == '/' and \
                               matrix[r2][c1] == '/' and \
                               matrix[r2][c2] == '\\':
                                return False
        return True

    def check_constraints(matrix):
        row_counts = [0] * R
        col_counts = [0] * C
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == '/':
                    row_counts[r] += 1
                    col_counts[c] += 1
        return row_counts == rows and col_counts == cols

    import itertools
    for combo in itertools.product(*[['/', '\\'] for _ in range(R * C)]):
        matrix = [list(combo[i*C:(i+1)*C]) for i in range(R)]
        if check_constraints(matrix) and is_square_free(matrix):
            return "POSSIBLE\n" + "\n".join("".join(row) for row in matrix)
    return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")