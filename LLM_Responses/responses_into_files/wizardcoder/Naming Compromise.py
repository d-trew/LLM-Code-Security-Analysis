import sys
from collections import defaultdict

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
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[-1][-1]

def find_compromise(s1, s2):
    m, n = len(s1), len(s2)
    min_edit_distance = float('inf')
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                edit_distances[s2[:j]] = edit_distance(s1, s2[:j])
            elif j == 0:
                edit_distances[s1[:i]] = edit_distance(s1[:i], s2)
            else:
                edit_distances[s1[:i] + s2[:j]] = min(edit_distances[s1[:i - 1] + s2[:j], dp[i][j - 1], dp[i - 1][j]) + 1)
    for i in range(m):
        for j in range(n):
            if edit_distances[s1[:i+1] + s2[:j+1]] < min_edit_distance:
                min_edit_distance = edit_distances[s1[:i+1] + s2[:j+1]]
    return s1[:-min_edit_distance] + s2[-min_edit_distance:]

def main():
    t = int(input())
    for i in range(t):
        cameron, jamie = input().split()
        edit_distances = defaultdict(int)
        compromise = find_compromise(cameron, jamie)
        print("Case #%d: %s" % (i+1, compromise) if len(compromise) > 0 else "Case #%d: No possible answer" % (i+1))

if __name__ == '__main__':
    main()