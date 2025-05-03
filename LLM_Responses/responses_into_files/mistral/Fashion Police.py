from itertools import combinations
import sys
input = sys.stdin.readline

def solve(j, p, s, k):
    if j == 1 or p == 1 or s == 1:
        return min(j, p, s)
    comb_set = set()
    for jacket, pants, shirt in combinations([i+1 for i in range(1, j+1)], 3):
        comb_set.add((jacket, pants))
        comb_set.add((pants, shirt))
        comb_set.add((jacket, shirt))
    if len(comb_set) > k:
        return 0
    days = [(jacket, pants, shirt) for jacket in range(1, j+1) for pants in range(1, p+1) for shirt in range(1, s+1)]
    outfits = set()
    for _ in range(min(j,p,s)):
        outfit = tuple(sorted(days.pop()))
        if outfit not in outfits and (outfit[0], outfit[1]) not in comb_set:
            outfits.add(outfit)
    return len(outfits)

T = int(input().strip())
for t in range(1, T+1):
    j, p, s, k = map(int, input().split())
    print("Case #{}: {}".format(t, solve(j,p,s,k)))


This program reads the number of test cases, then for each test case it reads the values J, P, S, and K. It calculates the maximum possible number of days to avoid Fashion Jail using the `solve()` function, which generates all combinations of jackets, pants, and shirts and checks if any combination appears more than K times. If so, it returns 0; otherwise, it returns the maximum number of unique outfits that can be formed without violating the Fashion Jail rules. Finally, it outputs the result for each test case.