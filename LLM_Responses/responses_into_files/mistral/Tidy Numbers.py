from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def is_tidy(n):
    digits = [int(d) for d in str(n)]
    return digits and all(digits[i] <= digits[j] for i, j in enumerate(range(len(digits))))

def solve(N):
    tidy_numbers = []
    for num in range(1, N + 1):
        if is_tidy(num):
            tidy_numbers.append(num)
    return tidy_numbers[-1]

T = int(stdin.readline())
for t in range(1, T+1):
    N = int(stdin.readline())
    print(f"Case #{t}: {solve(N)}")