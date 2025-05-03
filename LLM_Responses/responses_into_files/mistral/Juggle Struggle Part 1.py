import itertools
from collections import defaultdict

def magnificent_arrangement(positions):
    pairs = list(itertools.combinations(range(len(positions)), 2))
    graph = defaultdict(list)
    for i, (x1, y1), (x2, y2) in pairs:
        if abs(x1 - x2) + abs(y1 - y2) <= 2:
            graph[i].append(j)
            graph[j].append(i)
    for i, adjacencies in enumerate(graph.values()):
        if len(adjacencies) == 1 and i not in adjacencies:
            return [(i, adjacencies[0])] + list(zip(*sorted((p for p in pairs if p[0] != p[1] and (p[0], p[1]) not in graph), key=lambda x: x[0])))
    return []

T = int(input())
for _ in range(T):
    N = int(input())
    positions = [list(map(int, input().split())) for _ in range(2 * N)]
    result = magnificent_arrangement(positions)
    if result:
        print("Case #{}: {}".format(_ + 1, ' '.join(str(pair) for pair in result)))
    else:
        print("Case #{}: IMPOSSIBLE".format(_ + 1))


This Python code finds a magnificent arrangement of jugglers given their positions on the stage. It first generates all possible pairs of jugglers and builds a graph to represent potential collisions between chainsaws by connecting pairs that are at risk of collision. Then it checks if there exists any pair that has only one adjacent pair in the graph. If such a pair is found, it returns this pair as the solution. If no such pair is found, it returns an empty list indicating no valid arrangement exists for the given positions. The code then reads the number of test cases and processes each test case separately.