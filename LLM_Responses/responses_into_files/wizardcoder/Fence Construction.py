import sys

def is_valid(fences):
    for i in range(len(fences)):
        for j in range(i + 1, len(fences)):
            if i != j and (fences[i][0] == fences[j][2] and fences[i][1] == fences[j][3]) or (fences[i][2] == fences[j][0] and fences[i][3] == fences[j][1]):
                return False
    return True

def find_path(fences, start, end, visited):
    if start in visited:
        return []
    visited.add(start)
    for i in range(len(fences)):
        if fences[i][0] == start and (fences[i][2], fences[i][3]) not in visited:
            path = find_path(fences, (fences[i][2], fences[i][3]), visited)
            if path:
                return [i + 1] + path
        elif fences[i][2] == start and (fences[i][0], fences[i][1]) not in visited:
            path = find_path(fences, (fences[i][0], fences[i][1]), visited)
            if path:
                return [i + 1] + path
    return []

def build_order(fences):
    order = []
    while len(fences) > 0:
        start = (0, 0)
        end = fences[0][0], fences[0][1]
        path = find_path(fences, start, {(end[0], end[1])}, set())
        if not path:
            return "Impossible"
        order += path
        for i in range(len(fences)):
            if fences[i][2] == end[0] and fences[i][3] == end[1]:
                del fences[i]
    return order

T = int(input())
for t in range(1, T + 1):
    F, K = map(int, sys.stdin.readline().split())
    fences = []
    for i in range(K):
        A, B, C, D = map(int, input().split())
        fences.append((A, B, C, D))
    for i in range(F - K):
        A, B, C, D = map(int, input().split())
        if (C, D) not in [(a, b) for a, b, c, d in fences]:
            fences.append((A, B, C, D))
    if is_valid(fences):
        order = build_order(fences)
        print("Case #{}: {}".format(t, " ".join(map(str, order)))
    else:
        print("Case #{}: Impossible".format(t))