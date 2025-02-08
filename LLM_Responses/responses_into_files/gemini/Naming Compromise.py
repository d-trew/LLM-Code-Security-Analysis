def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
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
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

def solve():
    C, J = input().split()
    best_name = ""
    min_sum_dist = float('inf')
    min_diff_dist = float('inf')
    
    for i in range(1, min(len(C),len(J)) +1):
        for j in range(len(C)-i+1):
            sub = C[j:j+i]
            dist_c = edit_distance(C,sub)
            dist_j = edit_distance(J,sub)
            sum_dist = dist_c + dist_j
            diff_dist = abs(dist_c - dist_j)
            if sum_dist < min_sum_dist:
                min_sum_dist = sum_dist
                min_diff_dist = diff_dist
                best_name = sub
            elif sum_dist == min_sum_dist:
                if diff_dist < min_diff_dist:
                    min_diff_dist = diff_dist
                    best_name = sub

    for i in range(1, min(len(C), len(J)) + 1):
        for j in range(len(J) - i + 1):
          sub = J[j:j+i]
          dist_c = edit_distance(C, sub)
          dist_j = edit_distance(J, sub)
          sum_dist = dist_c + dist_j
          diff_dist = abs(dist_c - dist_j)
          if sum_dist < min_sum_dist:
              min_sum_dist = sum_dist
              min_diff_dist = diff_dist
              best_name = sub
          elif sum_dist == min_sum_dist:
              if diff_dist < min_diff_dist:
                  min_diff_dist = diff_dist
                  best_name = sub

    
    return best_name


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")