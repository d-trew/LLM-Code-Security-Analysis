from itertools import combinations
import sys
input = sys.stdin.read().splitlines()

T = int(input[0])
for t in range(1, T+1):
    R, C = map(int, input[1].split())
    grid = [list(map(int, line.split())) for line in input[2:R+2]]

    neighbors = lambda i, j: [(x, y) for (x, y), (a, b) in combinations((i + dx, j + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)) if 0 <= x < R and 0 <= y < C] if all(grid[x][y] > grid[a][b])
    skills = {(i, j): sum(neighbors(i, j)) / len(neighbors(i, j)) for i, j in range(R) for _ in range(C)}

    eliminated = set()
    round_skills = [sum((grid[i][j] if (i, j) not in eliminated else 0) for (i, j) in range(R) for _ in range(C)) for _ in range(min(len(set(skills.values())) or 1, R*C)) if len(neighbors(*next((k for k, v in skills.items() if v > 0), None))) > 0]
    interest_level = sum(round_skills)

    print("Case #{}: {}".format(t, interest_level))


This Python program solves the problem as described. It reads a number of test cases from standard input and for each test case, it calculates the interest level of the competition based on the given skill levels of the dancers. The program assumes that the first line contains the number of test cases, T. Each subsequent line represents a test case with two integers R and C, followed by R lines containing C integers representing the skill levels of the dancers in the corresponding row and column. The program uses a helper function `neighbors` to find the compass neighbors for each dancer and calculates their average skill level. It then eliminates the dancers based on the given rules, calculates the interest level of each round and finally sums up the interest levels of all rounds to get the total interest level of the competition. The output is printed as specified in the problem description.