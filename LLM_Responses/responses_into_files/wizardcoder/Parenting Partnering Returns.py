import sys
sys.setrecursionlimit(10**6)

def dfs(graph, visited, current, path):
    if len(path) == len(graph):
        return True
    for i in range(len(graph)):
        if not visited[i] and (current[-1][0] < graph[i][0] or current[-1][1] < graph[i][1]):
            visited[i] = True
            path.append((graph[i], i)
            if dfs(graph, visited, path) is True:
                return True
            else:
                path.pop()
                visited[i] = False
    return False

def find_schedule(activities):
    graph = [(a[1], a[2]) for a in activities]
    visited = [False] * len(graph)
    schedule = [''] * len(graph)
    dfs(graph, visited, [(0, 0)])
    for i in range(len(visited)):
        if not visited[i]:
            return "IMPOSSIBLE"
        else:
            schedule[i] = 'C' if activities[i][3] == 'C' else 'J'
    return ''.join(schedule)

n_cases = int(input())
for i in range(1, n_cases+1):
    N = int(input())
    activities = []
    for j in range(N):
        S, E, C = map(int, input().split())
        activities.append((S, E, C)
    schedule = find_schedule(activities)
    if schedule == "IMPOSSIBLE":
        print("Case #%d: IMPOSSIBLE" % i)
    else:
        print("Case #%d: %s" % (i, schedule)