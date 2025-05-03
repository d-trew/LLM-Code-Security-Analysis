T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    balls = [list(map(int, input().split())) for _ in range(N)]
    ans = 2 * (N - 1) + max(0, abs(balls[0][0]) - 1)
    print(f"Case # {_+1}: {ans}")