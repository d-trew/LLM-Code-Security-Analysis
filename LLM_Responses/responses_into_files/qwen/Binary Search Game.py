MOD = 10**9 + 7

def binary_search_game(N, M, L, A):
    from functools import lru_cache
    
    @lru_cache(None)
    def dp(left, right, turn):
        if left == right:
            return A[left]
        
        mid = (left + right) // 2
        if turn % 2 == 0:  # Alice's turn
            return max(dp(left, mid, turn + 1), dp(mid + 1, right, turn + 1))
        else:  # Bob's turn
            return min(dp(left, mid, turn + 1), dp(mid + 1, right, turn + 1))
    
    total_score = 0
    for cards in product(range(1, M+1), repeat=N):
        score = dp(0, len(A) - 1, 0)
        total_score += cards[score-1]
    
    return total_score % MOD

from itertools import product
import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])
index = 1
results = []

for _ in range(T):
    N = int(data[index])
    M = int(data[index + 1])
    L = int(data[index + 2])
    A = list(map(int, data[index + 3:index + 3 + (1 << L)]))
    index += 3 + (1 << L)
    
    result = binary_search_game(N, M, L, A)
    results.append(result)

for i, result in enumerate(results):
    print(f"Case #{i+1}: {result}")