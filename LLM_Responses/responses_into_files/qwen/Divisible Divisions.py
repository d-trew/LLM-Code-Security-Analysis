MOD = 10**9 + 7

def count_divisible_divisions(S, D):
    n = len(S)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            if int(S[j:i]) % D == 0:
                dp[i] += dp[j]
                dp[i] %= MOD
                
    return dp[n]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    index = 1
    for _ in range(T):
        S = data[index]
        D = int(data[index + 1])
        index += 2
        
        result = count_divisible_divisions(S, D)
        results.append(f"Case #{_+1}: {result}")
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()