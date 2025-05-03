from collections import deque

def max_customers(pancakes):
    pancakes = sorted([(i, x) for i, x in enumerate(pancakes)], key=lambda x: (-x[1], x[0]))
    dp = [0] * len(pancakes)
    longest_increasing_subsequence = []
    
    for _, (_, val) in pancakes:
        idx = bisect.bisect_left(longest_increasing_subsequence, val)
        if idx == len(longest_increasing_subsequence):
            longest_increasing_subsequence.append(val)
        else:
            longest_increasing_subsequence[idx] = val
        dp[-1] = max(dp[-1], idx+1)
    
    return len(deque(pancakes)) - dp[-1] + 1

T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    pancakes = list(map(int, input().strip().split()))
    print("Case #{}: {}".format(t+1, max_customers(pancakes)))