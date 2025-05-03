import sys
sys.setrecursionlimit(10**6)

def is_tidy(n):
    digits = [int(x) for x in str(n)]
    return all(digits[i] <= digits[i+1] for i in range(len(digits)-1))


for tc, n in enumerate(map(int, sys.stdin.readlines()):
    print("Case #{}: {}".format(tc+1, next(x for x in range(n, 0, -1) if is_tidy(x)))

# Example input:
# 2
# 50
# 999999999
# Output:
# Case #1: 89
# Case #2: 4897655531230

# Explanation:
# For the first test case, the last tidy number counted is 89. For the second test case,
# since we need to count down from 99999999, the next tidy number before that would be 489765531230.