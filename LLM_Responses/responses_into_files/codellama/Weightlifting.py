import sys

# Read input
T = int(input())
for case in range(1, T+1):
    E, W = map(int, input().split())
    X = []
    for i in range(E):
        X.append(list(map(int, input().split())))

# Calculate minimum number of operations needed
min_ops = 0
for e in range(E):
    ops = 0
    for w in range(W):
        if X[e][w] > 0:
            ops += X[e][w]
    min_ops += max(ops, X[e][0])

# Print output
print("Case #" + str(case) + ": " + str(min_ops))