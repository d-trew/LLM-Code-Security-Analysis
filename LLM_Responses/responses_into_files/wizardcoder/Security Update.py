import sys
from collections import defaultdict

def parse_input():
    T = int(sys.stdin.readline().strip())
    cases = []
    for t in range(T):
        C, D = map(int, input().split())
        X = list(map(int, input().split()))
        connections = defaultdict(set)
        for _ in range(D):
            U, V = map(int, input().split())
            connections[U].add(V)
            connections[V].add(U)
        cases.append((C, D, X, connections))
    return T, cases

def solve_case(C, D, X, connections):
    latencies = [-1] * (C+1)  # initialize all latencies to -1
    latencies[1] = 0  # source computer has zero latency
    
    def dfs(node, parent=-1):
        for child in connections[node]:
            if child == parent: continue  # skip back edges
            if latencies[child] != -1: continue  # already visited
            
            if X[node-2] >= 0 and X[child-2] < 0:
                latency = abs(X[node-2]) - abs(X[child-2])  # child received update before node
            else:
                latency = abs(X[node-2]) + abs(X[child-2])  # child received update after node
            
            if latency > 10**6: continue  # invalid latency value, skip this connection
            latencies[child] = latency
            dfs(child, node)
    
    dfs(1)  # start DFS from source computer
    return latencies[2:]  # remove the source computer and return only non-source computers' latencies

def main():
    T, cases = parse_input()
    for i, (C, D, X, connections) in enumerate(cases):
        latencies = solve_case(C, D, X, connections)
        print("Case #{}: {}".format(i+1), " ".join(map(str, latencies))

if __name__ == '__main__':
    main()