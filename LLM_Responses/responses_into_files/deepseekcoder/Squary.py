import sys
from collections import Counter
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    freq = Counter()
    for i in range(n):
        freq[arr[i]**2] += 1
        
    dp = [0] * (k + 1)
    squares_seen = set()
    
    for num in sorted(freq.keys(), key=abs):
        if num not in squares_seen:
            squares_seen.add(num)
            
            for i in range(k, -1, -1):
                dp[i] = max((dp[(i-j)] + j) % (k + 1), dp[i]) if freq[num] else dp[i]
                
        else:
            temp_freq = freq.copy()
            
            for i in range(k, -1, -1):
                temp_dp = dp[:]
                temp_dp[i % (k + 1)] += min((num // num) * freq[num], k - i + 1) if num >= 0 else 0
                
                for j in range(min(freq[num], k - i + 1)):
                    dp[(i + j) % (k + 1)] = max(dp[(i + j) % (k + 1)], temp_dp[(i - num) % (k + 1)])
                
                for _ in range(min(temp_freq[num], k - i + 1)):
                    freq[num] -= 1
                    
    return dp[-1] if dp[-1] else "IMPOSSIBLE"

t = int(input())
for tc in range(1, t + 1):
    print("Case #{}: {}".format(tc, solve()))