from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    T = int(input().strip())
    for t in range(T):
        F, K = map(int, input().split())
        fences = []
        for _ in range(F+K):
            x1, y1, x2, y2 = map(int, input().split())
            if (x1, y1) > (x2, y2):
                x1, y1, x2, y2 = x2, y2, x1, y1
            fences.append(((x1, y1), (x2, y2)))
        fences.sort()
        
        ans = []
        active_fence = fences[0]
        for i in range(1, len(fences)):
            if active_fence[1][0] < fences[i][0][0]:
                active_fence = fences[i]
            elif active_fence[1][1] > fences[i][1][1]:
                ans.append(i+K)
        print("Case #{}:".format(t+1), ' '.join(map(str, [x+1 for x in ans])))

solve()