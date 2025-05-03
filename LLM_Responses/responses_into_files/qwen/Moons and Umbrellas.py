def min_copyright_cost(X, Y, S):
    n = len(S)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if S[i] == 'C' and S[j] == 'J':
                dp[i][j] = min(X + dp[i+1][j], Y + dp[i][j-1])
            elif S[i] == 'J' and S[j] == 'C':
                dp[i][j] = min(Y + dp[i+1][j], X + dp[i][j-1])
            else:
                dp[i][j] = dp[i+1][j]
    
    return dp[0][-1]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        X = int(data[index])
        Y = int(data[index + 1])
        S = data[index + 2]
        index += 3
        
        result = min_copyright_cost(X, Y, S)
        results.append(f"Case #{_+1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()