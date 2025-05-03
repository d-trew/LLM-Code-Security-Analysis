import sys

# Read the input from stdin
n_cases = int(input())
for case in range(1, n_cases+1):
    n, r, p, s = map(int, input().split())
    # Check if it is possible to organize the lineup without ties
    if r + p + s != 2*n or r < 0 or p < 0 or s < 0 or n < 1:
        print("Case #{}: IMPOSSIBLE".format(case))
    else:
        # Create a list of all possible lineups
        lineups = []
        for i in range(n):
            for j in range(i+1, n):
                lineups.append("R"*r + "P"*p + "S"*s)
        # Sort the list alphabetically
        lineups.sort()
        print("Case #{}: {}".format(case, lineups[0]))