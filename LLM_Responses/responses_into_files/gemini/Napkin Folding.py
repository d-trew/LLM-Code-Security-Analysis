def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve():
    N, K = map(int, input().split())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    if K == 2:
        print("POSSIBLE")
        print(f"{points[0][0]}/{1} {points[0][1]}/{1} {points[N//2][0]}/{1} {points[N//2][1]}/{1}")
        return

    if K > N // 2 + 1 :
        print("IMPOSSIBLE")
        return

    print("IMPOSSIBLE")


T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: ", end="")
    solve()