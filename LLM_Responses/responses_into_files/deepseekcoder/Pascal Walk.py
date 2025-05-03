def pascal_walk(n):
    triangle = [[1], [1, 1]]
    s = 0
    while len(triangle) <= n:
        row = [1]
        for i in range(len(triangle[-1]) - 1):
            row.append(triangle[-1][i] + triangle[-1][i+1])
        row.append(1)
        triangle.append(row)
        s += len(triangle) - 1
    total = sum(int(x) for row in triangle for x in row)
    if total < n:
        return "Case #1: 1 1"
    else:
        for i, (row, pos) in enumerate(zip(triangle, range(1, s+1))):
            if total - sum(triangle[pos-1]) == int(row[0]):
                return f"Case #{pos}: {pos} {len(triangle[pos-1])}"
        return "Case #1: 1 1"

T = int(input())
for _ in range(T):
    n = int(input())
    print(pascal_walk(n))