T = int(input())
for _ in range(T):
    R, B = map(int, input().split())
    jugglers = min(R // 1 + (B - 1) // 1, R % 1 + (B - 1) % 1)
    print(f"Case #{_+1}: {jugglers}")