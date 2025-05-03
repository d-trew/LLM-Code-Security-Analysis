import sys

def dfs(i, fences, k, visited):
    if i >= len(fences):
        return True
    for j in range(len(fences)):
        if not visited[j] and (i == k or fences[i][0] != fences[j][0] or fences[i][1] != fences[j][1]):
            visited[j] = True
            if dfs(i + 1, fences, k, visited):
                return True
    return False

def solve(fences, k):
    for i in range(len(fences)):
        visited = [False] * len(fences)
        visited[k - 1] = True
        if not dfs(0, fences, k - 1, visited):
            return "Case #{}: Impossible".format(sys._getframe().f_lineno)
    return "Case #{}: {}".format(sys._getframe().f_lineno, ' '.join(map(str, range(1, len(fences) + 1))))

T = int(input())
for t in range(T):
    F, K = map(int, input().split())
    fences = []
    for i in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        fences.append(((x1, y1), (x2, y2)))
    print(solve(fences, K))