def find_a_b(N):
    for i in range(1, N):
        if '4' not in str(i) and '4' not in str(N - i):
            return i, N - i

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    A, B = find_a_b(N)
    print(f"Case #{t}: {A} {B}")