T = int(input())
for i in range(1, T + 1):
    S = input()
    K = int(input())
    pancake_flipper_flips = 0
    while True:
        if S[0] == '+':
            for _ in range(K):
                if len(S) < _ * (K - 1) + _:
                    break
                S = '+' * (_ * (K - 1) + _) + '-' * (len(S) - _ * (K - 1) - _) + S[_ * (K - 1):]
            pancake_flipper_flips += 1
        if all(c == '+' for c in S):
            break
    if all(c == '+' for c in S):
        print(f"Case #{i}: {pancake_flipper_flips}")
    else:
        print(f"Case #{i}: IMPOSSIBLE")