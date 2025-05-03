T = int(input())
for t in range(1, T+1):
    N = int(input())
    for a in range(1, N//2 + 1):
        b = N - a
        if '4' not in str(a) and '4' not in str(b):
            print(f"Case #{t}: {a} {b}")
            break