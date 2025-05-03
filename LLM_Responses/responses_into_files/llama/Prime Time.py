T = int(input())
for _ in range(T):
    M = int(input())
    primes = [int(input()) for _ in range(M)]
    N = [0] * (M + 1)
    for i, p in enumerate(primes):
        N[i] = int(input())
    max_score = 0
    for i in range(2 ** M):
        left_sum = 0
        right_product = 1
        for j in range(M):
            if ((i >> j) & 1):
                left_sum += primes[j] * N[j]
            else:
                right_product *= primes[j]
        max_score = max(max_score, min(left_sum, right_product))
    print(f"Case #{_ + 1}: {max_score}")