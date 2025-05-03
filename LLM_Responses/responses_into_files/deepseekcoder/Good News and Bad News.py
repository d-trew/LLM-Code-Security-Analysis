import sys
from collections import defaultdict

def check(graph, friends):
    for friend in range(1, friends + 1):
        if len(graph[friend]) == 0 or len(graph[-friend]) == 0:
            return False
    return True

def solve():
    T = int(input())
    for t in range(T):
        F, P = map(int, input().split())
        graph = defaultdict(list)
        for _ in range(P):
            a, b = map(int, input().split())
            if a != -b:
                graph[a].append(b)
                graph[-a].append(-b)
        ans = [0] * P
        flag = True
        for friend in range(1, F + 1):
            if len(graph[friend]) > 2 or (len(graph[-friend]) > 0 and len(graph[friend]) == 0):
                flag = False
                break
            elif len(graph[friend]) == 2:
                ans.append((abs(graph[friend][0] - graph[friend][1]) <= 2**F))
        if not flag or not check(graph, F):
            print('Case #{}: IMPOSSIBLE'.format(t + 1))
        else:
            print('Case #{}: {}'.format(t + 1, ' '.join(map(str, ans))))

solve()