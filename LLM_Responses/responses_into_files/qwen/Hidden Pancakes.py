from math import factorial

MOD = 10**9 + 7

def count_orders(N, V):
    dp = [[0] * (N + 1) for _ in range(1 << N)]
    dp[0][0] = 1
    
    for mask in range(1 << N):
        for i in range(N):
            if mask & (1 << i):
                prev_mask = mask ^ (1 << i)
                for j in range(i + 1):
                    if V[j] > V[i]:
                        dp[mask][i] += dp[prev_mask][j]
                        dp[mask][i] %= MOD
    
    result = sum(dp[(1 << N) - 1]) % MOD
    return result

def solve():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        V = list(map(int, input().split()))
        
        result = count_orders(N, V)
        
        print(f"Case #{t}: {result}")

if __name__ == "__main__":
    solve()