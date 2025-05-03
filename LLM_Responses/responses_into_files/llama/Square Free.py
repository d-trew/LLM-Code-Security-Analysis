T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    rows = list(map(int, input().split()))
    cols = list(map(int, input().split()))
    if sum(rows) != sum(cols):
        print("IMPOSSIBLE")
    else:
        matrix = [['/' for _ in range(C)] for _ in range(R)]
        row_idx = 0
        col_idx = 0
        forward_diags = 0
        backslash_diags = 0
        for r in rows:
            for _ in range(r):
                if forward_diags < sum(cols) // 2:
                    matrix[row_idx][col_idx] = '/'
                    forward_diags += 1
                else:
                    matrix[row_idx][col_idx] = '\\'
                    backslash_diags += 1
                col_idx = (col_idx + 1) % C
            row_idx += 1
        print("POSSIBLE")
        for row in matrix:
            print(''.join(row))