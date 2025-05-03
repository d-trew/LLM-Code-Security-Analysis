import sys

def solve(X):
    Y = []
    for i in range(len(X)):
        if len(str(X[i])) == 1:
            X[i] = int(str(X[i]) + '0')
        Y.append(X[i])
    return Y

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        X = list(map(int, input().split()))
        Y = solve(X)
        print("Case #" + str(t+1) + ": " + str(len(Y)))