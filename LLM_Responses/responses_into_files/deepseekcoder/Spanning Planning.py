Here is a Python program that generates a graph with the specified properties:


def generate_graph(K):
    # For K=1, we have a triangle (1-2, 1-3, 2-3)
    if K == 1:
        return [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    
    # For K=2, we have a cycle (1-2, 2-3, 3-4, 4-1) with two edges removed (1-3 and 2-4)
    if K == 2:
        return [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
    
    # For K=3, we have a triangle with one edge removed (1-2 and 2-3)
    if K == 3:
        return [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    
    # For K=4, we have a cycle with three edges removed (1-2, 2-3, 3-4)
    if K == 4:
        return [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
    
    # For larger K, we have a cycle with one edge removed for each additional spanning tree (K-1 edges)
    n = K + 2  # The number of nodes is at least K+2
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if i == 0 and j == n-1: continue
            graph[i][j] = 1
            graph[j][i] = 1
    return graph

T = int(input())  # Number of test cases
for tc in range(1, T+1):
    K = int(input())  # Desired number of spanning trees
    graph = generate_graph(K)
    
    print("Case #{}: {}".format(tc, len(graph)))
    for row in graph:
        print(''.join(map(str, row)))