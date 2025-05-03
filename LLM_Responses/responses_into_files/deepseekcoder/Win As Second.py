from collections import defaultdict

def dfs(node, parent):
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
    red_nodes.append(node)

T = int(input())
for _ in range(T):
    N = int(input())
    print((N-1)*'\n')  # Print empty lines for tree edges
    M = int(input())
    for _ in range(M):
        K = int(input().split()[0])
        red_nodes = []
        for node in input().split():
            dfs(int(node), -1)  # Perform DFS to find all red nodes
        if len(red_nodes) == N:
            print(-1)  # If all vertices are red, Ueli loses the game
        else:
            remaining = set(range(1, N+1)) - set(red_nodes)
            for node in remaining:
                neighbors = [str(x) for x in tree[node] if x not in red_nodes]
                print('\n'.join([str(len(neighbors)), ' '.join(sorted(neighbors))]))
    print()  # Print empty line after each test case