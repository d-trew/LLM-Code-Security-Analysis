import sys
from collections import defaultdict

def max_circle_size(n, friends):
    graph = defaultdict(list)
    for i, friend in enumerate(friends):
        graph[i].append(friend - 1)
        graph[friend - 1].append(i)

    used = [False] * n
    max_size = 0
    for i in range(n):
        if not used[i]:
            size, group = 1, [i]
            used[i] = True
            friend = graph[i][0]
            while friend != i:
                if not used[friend]:
                    size += 1
                    used[friend] = True
                    group.append(friend)
                    friend = graph[friend][0]
            max_size = max(max_size, size)

    return max_size

for _ in range(int(input())):
    n = int(input())
    friends = list(map(int, input().split()))
    print("Case #{}: {}".format(_ + 1, max_circle_size(n, friends)))


This program reads the number of test cases from the standard input and then iterates through each test case. For each test case, it first builds an undirected graph based on the given friendships using a defaultdict. Then, it iterates through all the nodes in the graph, starting with unvisited ones. If a node is visited, it checks if its unvisited friends can be added to the current group while maintaining the condition that each kid is sitting next to their BFF. The maximum group size found is returned at the end of the test case processing. Finally, the result for each test case is printed with the appropriate format.