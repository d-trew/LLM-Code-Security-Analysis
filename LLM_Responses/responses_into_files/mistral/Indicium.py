import itertools

def natural_latin_square(N, K):
    if N <= 0 or K < 1 or K > (N*N):
        return "IMPOSSIBLE"

    if N == 2 and K not in [2,4]:
        return "IMPOSSIBLE"

    squares = []

    for i in range(1, N+1):
        row = list(itertools.repeat(i, N))
        rows.append(row)

    for r1 in range(N):
        for r2 in range(r1 + 1, N):
            for c in range(N):
                if rows[r1][c] == rows[r2][c]:
                    row1 = rows[r1]
                    row2 = rows[r2]
                    a = row1.pop(c)
                    b = row2.pop(c)
                    row1[a-1], row2[b-1] = b, a

    trace = sum([rows[i][i] for i in range(N)])

    if trace != K:
        return "IMPOSSIBLE"

    for square in squares:
        print("Case #{}: POSSIBLE".format(casenum))
        for row in square:
            print(*row)
        casenum += 1
        print()

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    natural_latin_square(N, K)