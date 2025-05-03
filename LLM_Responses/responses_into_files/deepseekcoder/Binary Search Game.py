T = int(input())
for i in range(1, T + 1):
    N, M, L = map(int, input().split())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    total_score = 0
    for _ in range(M ** N):
        n = len(A)
        for j in range(L):
            mid = (n // 2) + ((n % 2) != 0)
            if A[mid - 1] < A[mid]:
                left_half = A[:mid]
                right_half = A[mid:]
            else:
                left_half = A[mid:]
                right_half = A[:mid]
            n //= 2
        total_score += (A[-1] % M) + 1
    print(f"Case #{i}: {total_score % MOD}")