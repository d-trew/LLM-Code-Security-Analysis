T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    max_straight = 0
    for s in set(S):
        if s > max_straight:
            max_straight = s
    print(f"Case #{_+1}: {max_straight}")