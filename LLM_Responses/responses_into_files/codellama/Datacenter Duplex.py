import sys
input = sys.stdin.readline
T = int(input())
for i in range(1, T + 1):
    R, C = map(int, input().split())
    matrix = []
    for j in range(R):
        matrix.append([])
        for k in range(C):
            matrix[j].append(input().strip())
    if check_connectivity(matrix, R, C) == "IMPOSSIBLE":
        print("Case #" + str(i) + ": IMPOSSIBLE")
    else:
        print("Case #" + str(i) + ": POSSIBLE")
        for j in range(R - 1):
            for k in range(C - 1):
                if matrix[j][k] == "A":
                    print("." if matrix[j + 1][k + 1] == "B" else "/", end="")
        print()
def check_connectivity(matrix, R, C):
    A = []
    B = []
    for j in range(C):
        for k in range(R):
            if matrix[k][j] == "A":
                A.append((k, j))
            elif matrix[k][j] == "B":
                B.append((k, j))
    if len(A) == 0 or len(B) == 0:
        return "IMPOSSIBLE"
    for i in range(R - 1):
        for j in range(C - 1):
            a = matrix[i][j]
            b = matrix[i + 1][j + 1]
            if (a == "A" and b == "B") or (a == "B" and b == "A"):
                return "IMPOSSIBLE"
    for i in range(R - 1):
        for j in range(C - 1):
            a = matrix[i][j]
            b = matrix[i + 1][j + 1]
            if (a == "A" and b == ".") or (a == "." and b == "B"):
                return "POSSIBLE"
    return "IMPOSSIBLE"