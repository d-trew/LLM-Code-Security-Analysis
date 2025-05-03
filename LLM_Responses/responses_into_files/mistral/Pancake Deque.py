import sys
from collections import deque
input = sys.stdin.readline

def max_payment(pancakes):
    q = deque(pancakes)
    payments = 1
    while len(q) > 1:
        max_right = max(q)
        max_left = min(q)
        if max_right - max_left >= max_right:
            break
        else:
            q.popleft()
            payments += 1
    return len(q) + payments

T = int(input())
for t in range(1, T+1):
    n = int(input())
    pancakes = list(map(int, input().split()))
    print(f"Case #{t}: {max_payment(pancakes)}")