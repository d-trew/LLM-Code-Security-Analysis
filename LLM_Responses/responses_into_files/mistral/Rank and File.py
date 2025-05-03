import sys
input = sys.stdin.readlines

def solve(N):
    heights = sorted([list(map(int, line.strip().split())) for _ in range(2*N-1)])
    rows = [[] for _ in range(N)]
    cols = [[] for _ in range(N)]

    for row_or_col, height in heights:
        if row_or_col % 2 == 0:
            rows[row_or_col // 2].append(height)
        else:
            cols[row_or_col - 1].append(height)

    missing = []
    for i in range(N):
        heights_in_row = set()
        for height in rows[i]:
            heights_in_row.add(height)
        if len(heights_in_row) != N:
            missing += sorted(list(set(cols[i]) - heights_in_row))

    return f"Case #{N}: {missing}"

for _ in range(int(input()[0])):
    N = int(input()[0])
    print(solve(N))

This program reads the number of test cases and solves each one individually. It first sorts the input lists by height, then separates them into rows and columns based on their position in the input. For each row, it creates a set of unique heights that appear in that row and compares it to all the heights in the corresponding column. If there are differences between the set of heights in the row and the column, it adds the missing heights to the `missing` list, which is then sorted and returned as the result for that test case.