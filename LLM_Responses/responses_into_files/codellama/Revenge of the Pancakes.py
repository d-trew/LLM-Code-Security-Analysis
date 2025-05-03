import sys

def solve(S):
    N = len(S)
    count = 0
    for i in range(N):
        if S[i] == '+':
            continue
        else:
            break
    if i == N - 1:
        return count
    else:
        count += 1
        for j in range(i + 1, N):
            if S[j] == '+':
                count += 1
                break
    return count

if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n_test = data[0]
    for i in range(1, n_test + 1):
        S = str(input())
        print("Case #{}".format(i), solve(S))