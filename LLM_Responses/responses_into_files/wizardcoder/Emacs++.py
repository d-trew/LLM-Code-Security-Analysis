import sys
from collections import deque

def parse_input():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        K, Q = map(int, input().split())
        P = list(map(str, input()))
        
        LRP = [list(map(int, input().split())) for _ in range(Q)]
        SRE = [list(map(int, input().split())) for _ in range(Q)]
        
        # process queries here and calculate time cost
        time_costs = []
        for i in range(Q):
            Li, Ri, Pi = LRP[i]
            Sj, Ej = SRE[i]
            
            if (Sj == 1 or P[Sj-2] == '(') and (Ej == K or P[Ej-1] == ')'):
                time_costs.append(abs(Li - Ri))
            else:
                # find the matching parenthesis for teleportation
                stack = deque()
                for j in range(Sj, Ej+1):
                    if P[j-1] == '(':
                        stack.append(j)
                    elif P[j-1] == ')':
                        stack.pop()
                    
                matching_parenthesis = stack[-1] if stack else -1
                time_costs.append((abs(Sj - Li) + abs(Ej - matching_parenthesis)) * Pi)
        
        print("Case #{}: {}".format(t+1, sum(time_costs))

parse_input()