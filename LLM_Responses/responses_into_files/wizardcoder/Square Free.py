import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def valid_matrix(r, c, rows, cols):
    if r == 0 and c == 0:
        return True
    if r < 0 or c < 0:
        return False
    if not (rows[r] or cols[c]):
        return False
    rows[r] -= 1
    cols[c] -= 1
    if valid_matrix(r-1, c, rows, cols) or valid_matrix(r, c-1, rows, cols):
        return True
    else:
        rows[r] += 1
        cols[c] += 1
        return False

def print_matrix(matrix, r, c, rows, cols):
    for i in range(r):
        row = []
        for j in range(c):
            if matrix[(i,j)]:
                row.append('/')
            else:
                row.append('\\')
        print("".join(row))

def solve_case(t, r, c, rows, cols):
    matrix = defaultdict(bool)
    for i in range(r):
        for j in range(c):
            if valid_matrix(i,j,rows,cols):
                matrix[(i,j)] = True
            else:
                matrix[(i,j)] = False
    print("Case #%d:" % (t+1), "POSSIBLE")
    print_matrix(matrix, r, c, rows, cols)

def main():
    t = int(input())
    for i in range(t):
        r,c = map(int, input().split())
        rows = list(map(int, input().strip().split()))[:r]
        cols = list(map(int, input().split())[:c])
        solve_case(i, r, c, rows, cols)
main()