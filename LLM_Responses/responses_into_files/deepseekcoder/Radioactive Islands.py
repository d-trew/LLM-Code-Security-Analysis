import sys
from scipy.optimize import minimize

def total_radiation(x):
    global islands, A, B
    t = 0
    radiation = 0
    for i in range(len(islands)):
        dist = ((0-islands[i][0])**2 + (B-islands[i][1]-x[i])**2)**0.5
        time_to_island = dist / abs(A - B) if x[i] != B else 0
        radiation += max((dist - time_to_island), 0) * 2 + (time_to_island if x[i] == B else 0)
    return radiation

T = int(sys.stdin.readline())
for case in range(1, T+1):
    N, A, B = map(float, sys.stdin.readline().split())
    islands = [list(map(float, sys.stdin.readline().split())) for _ in range(int(N))]
    res = minimize(total_radiation, [0]*len(islands), bounds=[(0, B)]*len(islands))
    print("Case #{}: {}".format(case, res.fun))