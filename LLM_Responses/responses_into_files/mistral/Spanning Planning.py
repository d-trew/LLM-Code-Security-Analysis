from itertools import combinations
import sys

def create_graph(nodes, edges):
    graph = [[0] * nodes for _ in range(nodes)]
    for edge in edges:
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1
    return graph

def num_spanning_trees(graph):
    n = len(graph)
    adjacency_matrix = [[0] * (n * n) for _ in range(n)]

    for i, row in enumerate(graph):
        for j, val in enumerate(row):
            if val:
                adjacency_matrix[i][i + j * n] = 1
                adjacency_matrix[i + j * n][i] = 1
    return sum(1 for c in combinations(range(n), 2) if all(adjacency_matrix[c[0]][c[1]] and adjacency_matrix[c[1]][c[0]]))

def main():
    T = int(input())
    for _ in range(T):
        K = int(input())
        if 3 <= K <= 22:
            nodes = 2 + (K - 1) // 2
            edges = []
            for i in range(nodes):
                for j in range(i + 1, nodes):
                    if len(edges) < K - 1:
                        edges.append((i, j))
            graph = create_graph(nodes, edges)
            print(f'Case #{_+1}: {nodes}')
            print(' '.join(' '.join(str(x) for x in row) for row in graph))
            print(f'Number of spanning trees: {num_spanning_trees(graph)}')
        else:
            print(f'Case #{_+1}: Invalid number of nodes')

if __name__ == '__main__':
    main()