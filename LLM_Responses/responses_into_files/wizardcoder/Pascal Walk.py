import itertools
import math

def binomial_coefficient(n, k):
    return math.comb(n, k) % (10**9 + 7)

def pascal_triangle():
    triangle = [[1]]
    for i in range(1, 51):
        row = [binomial_coefficient(i, j) for j in range(i+1)]
        triangle.append(row)
        yield row

def find_pascal_walk():
    n = int(input())
    print("Case #{}".format(n))
    walk = [(1, 1)]
    for i, row in enumerate(pascal_triangle()):
        if sum(row) == n:
            print(" ".join([str(i+1) for i in range(len(walk))]))
            return
        elif sum(row) > n:
            break
        else:
            max_index = row.index(max(row[:-1]) + 1)
            walk.append((i+1, max_index))
    print(" ".join([str(i+1 for i in range(len(walk)))])
        
for _ in range(int(input())):
    find_pascal_walk()