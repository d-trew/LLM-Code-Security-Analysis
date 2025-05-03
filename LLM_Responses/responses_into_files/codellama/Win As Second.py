import sys

def ueli_turn(N):
    # Choose a vertex to color red
    vertex = 1
    # Choose a subset (possibly none or all) of its blue neighbors to color red
    neighbors = [2, 3]
    return vertex, neighbors

def vreni_turn(N):
    # Choose a tree with N} vertices
    tree = {1: [2], 2: [3], 3: []}
    return tree

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        N = int(sys.stdin.readline())
        vertex, neighbors = ueli_turn(N)
        tree = vreni_turn(N)
        M = int(sys.stdin.readline())
        for m in range(M):
            # Process some number of exchanges until the game is over
            exchange = sys.stdin.readline()
            if vertex not in tree:
                # Ueli's turn
                K, A = exchange.split()
                K = int(K)
                A = [int(a) for a in A]
                if len(A) != K or any(a not in range(1, N+1) for a in A):
                    print(-1)
                    break
                vertex = A[0]
                neighbors = A[1:]
            else:
                # Vreni's turn
                if vertex not in tree:
                    print(-1)
                    break
                vertex = next(iter(tree - {vertex}))
                neighbors = [v for v in tree[vertex] if v != vertex]
            print(len(neighbors), *neighbors)