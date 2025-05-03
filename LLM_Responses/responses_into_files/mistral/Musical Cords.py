import math
from collections import defaultdict, namedtuple
import sys
input = sys.stdin.readline

def distance(i, j):
    return math.sqrt((R ** 2) - ((R * (D[j] - D[i])) ** 2))

def main():
    T = int(input())

    for _ in range(T):
        N, R, K = map(int, input().split())
        D, L = [], []
        for _ in range(N):
            Di, Li = map(int, input().split())
            D.append(Di)
            L.append(Li)

        edges = list(combinations(range(1, N + 1), 2))
        cords = sorted([(edge[0], edge[1], distance(edge[0], edge[1]) + L[edge[0]] + L[edge[1]]) for edge in edges], reverse=True)

        print("Case #{}:".format(_+1))
        for i, (a, b, l) in enumerate(cords[:K]):
            print(" {}".format(l))

from itertools import combinations

# For Python 3.6 and below
combinations = itertools.combinations


This code reads the test cases from standard input, calculates the distance between each pair of attachment points, sorts the cords by their length in descending order, and outputs the longest K cords for each test case. The `combinations()` function is used to generate all possible pairs of attachment points. For Python 3.6 and below, the built-in `combinations()` function should be replaced with the one defined above.