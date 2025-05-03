import sys
from collections import defaultdict

def read_input():
    num_cases = int(sys.stdin.readline().strip())
    cases = []
    for i in range(1, num_cases + 1):
        n = int(sys.stdin.readline().strip())
        holes = defaultdict(set)
        for j in range(n):
            x, y = map(int, sys.stdin.readline().strip().split())
            holes[(x, y)].add((x, y))
        cases.append(holes)
    return num_cases, cases

def count_distinct_holes(holes):
    max_count = 0
    for start in holes:
        visited = set()
        current = start
        count = 1
        while True:
            next_hole = None
            for hole in holes[current]:
                if hole not in visited:
                    next_hole = hole
                    break
            else:
                break
            if not next_hole:
                break
            visited.add(next_hole)
            count += 1
            current = next_hole
        max_count = max(max_count, count)
    return max_count

def main():
    num_cases, cases = read_input()
    for i in range(num_cases):
        print("Case #%d: %d" % (i+1, count_distinct_holes(cases[i]))

if __name__ == "__main__":
    main()