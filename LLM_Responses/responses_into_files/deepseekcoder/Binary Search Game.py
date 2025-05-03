import sys
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9 + 7

def solve(N, M, L, A):
    dp_min = [0] * (1 << L)
    dp_max = [0] * (1 << L)
    
    for i in range(L-1, -1, -1):
        n = 1 << i
        m = 2 * n
        
        cards = defaultdict(int)
        for j in range(m):
            cards[A[j]] += 1
            
        dp_min_next = [0] * (1 << L)
        dp_max_next = [0] * (1 << L)
        
        for mask in range(1, m):
            if bin(mask).count('1') == n:
                min_val = 1e9
                max_val = 0
                
                for sub_mask in range(mask):
                    if ((sub_mask & mask) == 0 and (sub_mask | mask) == m-1):
                        min_val = min(min_val, dp_min[sub_mask] + cards[max(A[j] for j in range(m) if ((sub_mask >> j) & 1))])
                        max_val = max(max_val, dp_max[sub_mask] + cards[max(A[j] for j in range(m) if ((sub_mask >> j) & 1))])
                
                dp_min_next[mask] = min_val % MOD
                dp_max_next[mask] = max_val % MOD
        
        dp_min, dp_max = dp_min_next, dp_max_next
    
    return sum(dp_min) * 2 % MOD if L % 2 == 0 else (sum(dp_min) + sum(dp_max)) % MOD

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    A = list(map(int, input().split()))
    
    print("Case #{}: {}".format(t, solve(N, M, L, A)))