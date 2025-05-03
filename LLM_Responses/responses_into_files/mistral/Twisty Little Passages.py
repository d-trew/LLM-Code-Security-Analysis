from collections import defaultdict
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    graph = defaultdict(int)
    connections = defaultdict(list)
    for _ in range(N-1):
        u, v = map(int, input().split())
        graph[u] += 1
        graph[v] += 1
        connections[u].append(v)
        connections[v].append(u)
    count = 0
    room = 1
    for _ in range(K+1):
        passages = graph[room] // 2 + 1
        count += passes
        if _ == K:
            print(count * 3 // 2, end='\n')
            break
        else:
            next_room = connections[room][random.randint(0, graph[room]-1)]
            room = next_room


This code reads the number of test cases (T), then processes each test case by first creating a graph to represent the cave and its passages. It uses two dictionaries: one to store the number of passages connected to each room, and another to store the connections between rooms. After that, it simulates the exploration of the cave by performing up to K+1 operations. The i-th operation is either an estimation or a movement through a passage. If the i-th operation is an estimation, it adds the number of passages connected to the current room to the count and outputs the estimate at the end if it's the last operation. Otherwise, it chooses a random passage from the ones available in the current room and moves to the next room. The code uses Python's built-in `random` module for choosing a random passage.