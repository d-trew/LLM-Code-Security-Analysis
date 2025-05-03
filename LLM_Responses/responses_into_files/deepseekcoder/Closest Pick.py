from collections import Counter
import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    counter = Counter(nums)
    keys = sorted(counter.keys(), reverse=True)
    
    for i in range(len(keys)-1):
        if abs(keys[i] - k/2) < abs(keys[i+1] - k/2):
            return "Case #{}: {:.7f}".format(t, 0.5)
    
    return "Case #{}: {:.7f}".format(t, 0 if keys[-1] > k-keys[-1] else 0.5)

T = int(input())
for t in range(1, T+1):
    print(solve())