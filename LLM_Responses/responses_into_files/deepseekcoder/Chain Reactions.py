import sys
sys.setrecursionlimit(10**9)

def max_fun(i):
    if visited[i]: return fun[i]
    visited[i] = True
    if points[i] != 0: 
        fun[i] = max(max_fun(points[i]-1), fun[i])
    return fun[i]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    fun = list(map(int, input().split()))
    points = list(map(int, input().split()))
    
    visited = [False]*n
    total_fun = 0
    for i in range(n):
        if not visited[i]: 
            total_fun += max_fun(i)
            
    print("Case #%d: %d" % (tc, total_fun))