def solve():
    L, U = map(int, input().split())
    N = L  # Choose a value from the range [L, U]

    print(N)
    
    # Create a star network.  Node 1 connects to all other nodes.
    for i in range(2, N + 1):
        print(1, i)
    for i in range(2, N + 1):
        print(i, 1)

    import sys
    sys.stdout.flush()

    received_N = int(input())
    assert received_N == N

    edges = []
    for _ in range(2 * (N -1)):
        u, v = map(int, input().split())
        edges.append((u,v))

    # Recover the permutation
    mapping = {}
    mapping[1] = 1 # Node 1 maps to itself in the star network

    connected_nodes = set()
    for u,v in edges:
      connected_nodes.add(u)
      connected_nodes.add(v)
    
    center_node = list(connected_nodes)[0]
    for i in range(1,N):
      u,v = edges[i*2-2]
      if u == center_node:
        mapping[i+1] = v
      else:
        mapping[i+1] = u
        
    

    result = [0] * N
    for i in range(1, N + 1):
        result[i - 1] = mapping[i]

    print(*result)
    sys.stdout.flush()


T = int(input())
for _ in range(T):
    solve()