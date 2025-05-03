import sys

def solve(n):
    a = list(range(1, n+1))
    b = []
    for i in range(2*n):
        if i < n:
            b.append(a[i])
        else:
            b.append(a[i-n]+n)
    return a, b

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a, b = solve(n)
        print(*a)
        print(*b)