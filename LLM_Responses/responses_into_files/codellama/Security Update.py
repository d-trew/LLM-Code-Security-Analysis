import sys

def solve(test_case):
    # Read input
    C, D = map(int, input().split())
    X = list(map(int, input().split()))
    Y = []
    for _ in range(D):
        Y.append(list(map(int, input().split())))
    
    # Initialize latencies to 0
    latencies = [0] * D
    
    # Compute latencies based on X values
    for i in range(1, C):
        if X[i] > 0:
            latencies[X[i] - 1] = abs(i - 1)
    
    # Print output
    print("Case #{}".format(test_case))
    for i in range(D):
        print("{} {}".format(latencies[i], Y[i][0]), end=" ")
    print()

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        solve(t)