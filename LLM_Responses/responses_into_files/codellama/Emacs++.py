import sys

def solve(P, L, R, PI):
    # Calculate the shortest time for each query
    N = len(L)
    ans = 0
    for i in range(N):
        l, r, p = L[i], R[i], PI[i]
        if l == r:
            ans += 1
        else:
            ans += max(abs(l - r), abs(p - l) + abs(r - p))
    return ans

def main():
    T = int(input())
    for t in range(T):
        K, Q = map(int, input().split())
        P = input()
        L, R, PI = [], [], []
        for _ in range(Q):
            L.append(int(input()))
            R.append(int(input()))
            PI.append(int(input()))
        ans = solve(P, L, R, PI)
        print("Case #" + str(t+1) + ": " + str(ans))

if __name__ == "__main__":
    main()