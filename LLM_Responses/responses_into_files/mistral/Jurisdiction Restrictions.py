from sys import stdin, setrecursionlimit
setrecursionlimit(3000)

def min_diff():
    for _ in range(int(stdin.readline())):
        R, C, S = map(int, stdin.readline().split())
        grid = [[False] * C for _ in range(R)]
        stations = []
        for _ in range(S):
            ri, ci, di = map(int, stdin.readline().split())
            if not grid[ri-1][ci-1]:
                grid[ri-1][ci-1] = True
                stations.append((ri, ci, di))

        assignments = [0]*S
        blocks_count = R*C - len([x for x in grid if x])
        for station in stations:
            assigned_blocks = []
            for i in range(max(0, station[0]-station[2]), min(station[0]+station[2]+1, R+1)):
                for j in range(max(0, station[1]-station[2]), min(station[1]+station[2]+1, C+1)):
                    if grid[i-1][j-1]:
                        assigned_blocks.append((i, j))
                        grid[i-1][j-1] = False
                        blocks_count -= 1
            assignments[stations.index(station)] += len(assigned_blocks)

        min_assignments = max(assignments)
        max_assignments = min(assignments)
        print(f"Case #{stdin.readline().strip()}: {max_assignments - min_assignments}")

min_diff()


This code reads the input, processes it, and outputs the solution for each test case as required by the problem description. The code assumes that the input is given line-by-line in the format specified in the description.