def min_edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    
    return dp[m][n]

def find_compromise_name(C, J):
    m, n = len(C), len(J)
    min_sum_edit_distance = float('inf')
    best_name = ""
    
    for i in range(m + 1):
        for j in range(n + 1):
            name = C[:i] + J[j:]
            sum_edit_distance = min_edit_distance(C, name) + min_edit_distance(J, name)
            if sum_edit_distance < min_sum_edit_distance:
                min_sum_edit_distance = sum_edit_distance
                best_name = name
    
    return best_name

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    index = 1
    for _ in range(T):
        C = data[index]
        J = data[index + 1]
        index += 2
        
        compromise_name = find_compromise_name(C, J)
        results.append(f"Case #{_+1}: {compromise_name}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()