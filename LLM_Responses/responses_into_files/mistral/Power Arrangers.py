import itertools
import sys
from collections import deque

def solve(t, f):
    for _ in range(t):
        missing_set = list(range(5))
        random.shuffle(missing_set)
        remaining_sets = list(itertools.permutations(range(1, 6)))
        random.shuffle(remaining_sets)

        figures = deque([0]*f+missing_set)
        visited = set()
        exchanges = deque([])

        for _ in range(f+1):
            figure = figures.popleft()
            if figure not in visited:
                exchanges.append((figure, figures.index(figure)))
                visited.add(figure)

        figure = figures.pop()
        index = figures.index(figure)
        exchanges.append((figure, index))

        answer = exchanges[f]
        print(" ".join(map(str, answer)))

import random
random.seed(int(sys.argv[1]))
solve(*map(int, input().split()))