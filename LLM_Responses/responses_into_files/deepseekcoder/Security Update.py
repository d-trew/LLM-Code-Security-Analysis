from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for t in range(1, T+1):
        C, D = map(int, input().split())
        X = list(map(int, input().split()))
        edges = defaultdict(list)
        for _ in range(D):
            u, v = map(int, input().split())
            edges[u].append(v)
            edges[v].append(u)
        
        res = [0]*D
        min_latency = 10**6 + 7
        for i in range(2, C+1):
            if X[i-1] < 0:  # computer i received the update before computer 1
                continue
            
            # find all computers that are connected to computer i and have received the update after computer 1
            for j in edges[i]:
                if X[j-1] > 0:  
                    res[X[j-1]-1] = max(res[X[j-1]-1], abs(X[i-1] - X[j-1]))
        
        print("Case #%d:" % t, end=" ")
        for i in range(D):
            if res[i] == 0:  # no latency value has been assigned to connection i yet
                res[i] = min_latency  
            print(res[i], end=" ")
        print()

solve()