import sys
input = sys.stdin.readline

def solve(R, C, S):
    # Initialize the matrix with the correct number of forward slash diagonals
    matrix = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if S[i] > 0:
                matrix[i][j] = '/'
                S[i] -= 1
            elif S[i] < 0:
                matrix[i][j] = '\\'
                S[i] += 1
    # Check if the matrix is square free
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '/':
                if i + 1 < R and matrix[i+1][j] == '\\' or j + 1 < C and matrix[i][j+1] == '/':
                    return "IMPOSSIBLE"
            elif matrix[i][j] == '\\':
                if i - 1 >= 0 and matrix[i-1][j] == '/' or j - 1 >= 0 and matrix[i][j-1] == '\\':
                    return "IMPOSSIBLE"
    # Print the matrix
    for i in range(R):
        print("".join(matrix[i]))
    return "POSSIBLE"

# Read input
T = int(input())
for case in range(1, T+1):
    R, C = map(int, input().split())
    S = list(map(int, input().split()))
    if solve(R, C, S) == "IMPOSSIBLE":
        print("Case #%d: IMPOSSIBLE" % case)
    else:
        print("Case #%d: POSSIBLE" % case)