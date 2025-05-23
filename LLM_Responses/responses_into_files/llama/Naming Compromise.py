from itertools import permutations

def edit_distance(s1, s2):
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
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

def find_compromise_name(c, j):
    min_distance = float('inf')
    best_name = ''
    for p in permutations(set(c)):
        name = ''.join(p)
        distance_c = edit_distance(c, name)
        distance_j = edit_distance(j, name)
        if distance_c + distance_j < min_distance:
            min_distance = distance_c + distance_j
            best_name = name
    return best_name

t = int(input())
for i in range(t):
    c, j = input().split()
    print(f'Case #{i+1}: {find_compromise_name(c, j)}')