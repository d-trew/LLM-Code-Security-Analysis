from itertools import cycle, count
import random

def beat(a, b):
    if a == 'R' and b == 'S': return True
    elif a == 'P' and b == 'R': return True
    elif a == 'S' and b == 'P': return True
    else: return False

def solve(programs):
    cycles = [cycle([c]) for c in set(sum(programs, []))]
    while True:
        winners = {}
        for i, p1 in enumerate(programs):
            p2 = (i + 1) % len(programs)
            if i not in winners or beat(next(cycles[winners[i]], p1[0]), next(cycles[p2], programs[p2][0])):
                winners[i] = p2
        if len(winners) == 1:
            return next(cycles[list(winners.keys())[0]])

T = int(input())
for _ in range(T):
    A = int(input())
    programs = [input() for _ in range(A)]
    if len(set(sum(programs, []))) < A:
        print("IMPOSSIBLE")
    else:
        print("Case #{}: {}".format(_ + 1, solve(programs)))