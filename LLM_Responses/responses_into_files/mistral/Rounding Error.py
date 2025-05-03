import sys
from collections import defaultdict
input = sys.stdin.readlines

def max_sum(n, l, c):
    freq = defaultdict(int)
    total = sum(c)
    for i in c:
        freq[i] += 1

    max_val = max(freq.values())
    return (total // max_val + 1) * max_val if total % max_val == 0 else (total // max_val + 2) * max_val

T = int(input().strip())
for t in range(1, T+1):
    n, l = map(int, input().split())
    c = list(map(int, input().split()))
    print(f"Case #{t}: {max_sum(n, l, c)}")