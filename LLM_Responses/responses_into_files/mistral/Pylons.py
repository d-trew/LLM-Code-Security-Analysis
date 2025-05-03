import sys
from itertools import permutations

def is_valid(r, c, dr, dc):
    return (r + dr) != prev[0] and (c + dc) != prev[1] \
           and ((abs(dr) == abs(dc)) or not (abs(r - prev[0]) == abs(c - prev[1])))

def solve(r, c):
    visited = set()
    prev = (r, c)
    visited.add((r, c))

    candidates = [(dr, dc) for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1))]
    candidates = [(dr, dc) for dr, dc in candidates if is_valid(r, c, dr, dc)]

    perms = list(permutations(candidates))
    for perm in perms:
        path = []
        for move in perm:
            r, c = r + move[0], c + move[1]
            path.append((r, c))
            visited.add((r, c))

            candidates = [(dr, dc) for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1))]
            candidates = [(dr, dc) for dr, dc in candidates if is_valid(r, c, dr, dc)]

            if len(visited) == r * c:
                return path

    return None

def print_result(case, solution):
    if solution is None:
        print(f'Case #{case}: IMPOSSIBLE')
    else:
        for i, (r, c) in enumerate(solution, start=1):
            print(f'Case #{case}: {["P" if i == 1 else ""]}{chr(65 + c - 1)}{chr(ord("A") + r - 1)}')

def main():
    for _ in range(int(sys.stdin.readline())):
        r, c = map(int, sys.stdin.readline().split())
        solution = solve(0, 0)
        print_result(_ + 1, solution)

if __name__ == '__main__':
    main()


This program reads the number of test cases and iterates through each one. For each test case, it calculates the possible valid moves from a given cell and generates all permutations of those moves. If a sequence of moves visits every cell exactly once without revisiting any cell, it returns that sequence as the solution. Otherwise, it returns None. The print_result function prints the appropriate output for each test case based on whether a solution was found or not.