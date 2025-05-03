import sys
from collections import defaultdict, Counter

def trace(matrix):
    return sum([matrix[i][i] for i in range(len(matrix))])

def check_latin_square(matrix):
    rows = [set(row) for row in matrix]
    cols = [set(col) for col in zip(*matrix)]
    if all(len(row) == 1 and len(col) == 1 for row, col in zip(rows, cols)):
        return True
    else:
        r_count = Counter([len(row) for row in rows] + [len(col) for col in cols])
        return False, r_count[1], len(r_count[1]) if r_count[1] else 0, r_count[2] if r_count[2] else 0

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        matrix = []
        for _ in range(N):
            row = list(map(int, input().split()))
            matrix.append(row)
        k, r, c = trace(matrix), 0, 0
        if not check_latin_square(matrix):
            r, c = check_latin_square(matrix)[1], check_latin_square(matrix)[2]
        print(f"Case #{_+1}: {k} {r} {c}")

solve()


This Python program reads the number of test cases from the input and then iterates through each test case. For each test case, it first computes the trace of the given matrix using the `trace()` function and checks if the matrix is a Latin square using the `check_latin_square()` function. If the matrix is not a Latin square, it calculates the number of rows and columns with repeated elements using the `check_latin_square()` function. Finally, it prints the result for each test case in the required format.