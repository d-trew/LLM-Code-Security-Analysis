import sys
input = sys.stdin.read()
t=int(input[0])
for i in range(1,t+1):
    n = int(input[i])
    matrix = []
    for j in range(n):
        matrix.append([int(x) for x in input[j+2].split()])
    trace=0
    repeated_rows = 0
    repeated_cols = 0
    for row in matrix:
        if len(set(row)) != n:
            repeated_rows += 1
    for col in zip(*matrix):
        if len(set(col)) != n:
            repeated_cols += 1
    trace = sum([x for x in matrix[i][i] for i in range(n)])
    print("Case #{} {} {}".format(i,trace,repeated_rows+repeated_cols))