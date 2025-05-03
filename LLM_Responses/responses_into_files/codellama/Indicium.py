import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t + 1):
    n, k = map(int, input().split())
    if n * n < k or k > n * n:
        print(f"Case #{i}: IMPOSSIBLE")
    else:
        print(f"Case #{i}: POSSIBLE")
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if j == k:
                    print(j, end=" ")
                else:
                    print(0, end=" ")