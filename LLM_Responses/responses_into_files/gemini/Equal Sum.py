T = int(input())
for _ in range(T):
    N = 100
    A = [2**i for i in range(N)]
    print(*A)
    B = list(map(int, input().split()))
    total_sum = sum(A) + sum(B)
    subset1 = []
    subset1_sum = 0
    for i in range(N):
        if subset1_sum + A[i] <= total_sum // 2:
            subset1.append(A[i])
            subset1_sum += A[i]
    remaining_sum = total_sum // 2 - subset1_sum
    for i in range(N):
        if remaining_sum >= B[i]:
            subset1.append(B[i])
            remaining_sum -= B[i]

    print(*subset1)