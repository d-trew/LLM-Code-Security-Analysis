import sys
from itertools import combinations

def get_graph(n):
    graph = [[] for _ in range(n)]
    for _ in range(n):
        line = list(map(int, sys.stdin.readline().strip()))
        for i, val in enumerate(line):
            if val == 1:
                graph[i].append((i, _))
    return graph

def min_lessons(graph):
    n = len(graph)
    can_operate = [[0]*n for _ in range(n)]
    for worker, machines in enumerate(graph):
        for machine in machines:
            can_operate[machine] |= (1 << worker)

    # Find all combinations of workers that can operate a machine
    combos = set()
    for i in range(1, 2**len(can_operate)):
        if any(not (i & c) for c in combinations([j for j in range(len(can_operate)) if can_operate[j][0] > 0], 2)):
            continue
        combos.add(i)

    # For each possible combination, find the minimum number of lessons needed to make it unique among all combinations
    least_common = {}
    for combo in combos:
        least_common[combo] = len(combos)

    min_lessons = 0
    for i, machine in enumerate(graph):
        workers = [w for w, machines in enumerate(graph) if machine and (can_operate[machine][i] != (1 << i)): ]
        if not workers:
            continue
        needed_lessons = float('inf')
        for combo in combos:
            if (combo >> workers[0]) & 1:
                needed_lessons = min(needed_lessons, least_common[combo])
        min_lessons += len(workers) * needed_lessons
    return min_lessons

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print("Case #{}: {}".format(_+1, min_lessons(get_graph(n))))


This Python program reads the number of test cases from standard input and then iterates through each case. For each test case, it first parses the graph representing the knowledge of workers about machines. Then it determines all possible combinations of workers who can operate a machine. After that, for each machine without an operator, it finds the minimum number of lessons needed to make the combination unique among all combinations and adds it to the total cost. Finally, it outputs the result for each test case.