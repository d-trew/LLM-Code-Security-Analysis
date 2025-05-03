def find_sum(n):
    for a in range(1, n+1):
        if '4' not in str(a) and (n-a)%10 != 4:
            b = n - a
            print(f"Case #{case}: {a} {b}")
            break

T = int(input())
for case in range(1, T+1):
    N = int(input())
    find_sum(N)