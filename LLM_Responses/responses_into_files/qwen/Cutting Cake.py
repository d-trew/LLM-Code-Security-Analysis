from math import inf
def solve():
    T = int(input())
    for _ in range(T):
        N, W, H = map(int, input().split())
        P, Q, R, S = map(int, input().split())
        A = [0] * N
        B = [0] * N
        for i in range(N):
            X, Y, a, b = map(float, input().split())
            A[i] = int(a)
            B[i] *int(b)
        a, b = inf, 0
        for i in range(N):
            area_left = max(0, (X + P - W) * Q - ((X + P) * Y + Q * H))
            area_right = max(0, (R - X) * S - ((R * Y + S * H)))
            a_left, b_left = 0, 0
            for j in range(i):
                a_left += max(0, (X + P - W) * Q - ((X + P) * Y + Q * H)) / (A[j] + B[j])
                b_left += max(0, (R - X) * S - ((R * Y + S * H)))
            a_right = 0
            for j in range(i, N):
                a_right -= max(0, (X + P - W) * Q - ((X + P) * Y + Q * H)) / (A[j] + B[j])
                b_right += max(0, (R - X) * S - ((R * Y + S * H)))
            if abs(a_left + a_right - b_left - b_right) < abs(a - b):
                a, b = a_left + a_right, b_left + b_right
        print(f"Case # {_ + 1}: {a} / {b}")