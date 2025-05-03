import random
from collections import defaultdict, deque

def binomial_coefficient(n, k):
    return int((fact[n] * fact[k]) // fact[k - n])

def solve(balls, max_bumps):
    fact = [1, 1] + [x * i for x, i in enumerate(range(2, 101))]
    n = len(balls)
    boxes = list(range(1, n+1))

    def shuffle_box(c):
        q = deque([i for i, x in enumerate(boxes) if x == c])
        if not q:
            return
        b = random.choice(q)
        balls[b - 1], boxes[b - 1] = balls[-1], boxes[b - 1]
        del boxes[b - 1]
        del balls[-1]

    def count_sorted():
        cnt = [0] * n
        for ball in balls:
            cnt[ball - 1] += 1
        return sum(1 for i, c in enumerate(cnt) if c == n-1)

    bumps = 0
    while count_sorted() != n:
        for i in range(n):
            boxes[i] = random.choice([x for x in range(1, n+1) if balls[x - 1] == i + 1])
        bumps += 1
        if max_bumps and bumps >= max_bumps:
            return -1
        c = (sum(balls) + bumps + 1) % n
        shuffle_box(c)
    return bumps

T, N, K = map(int, input().split())
for _ in range(T):
    balls = list(map(int, input().split()))
    result = solve(balls, K // N)
    if result == -1:
        print(-1)
    else:
        print(result)