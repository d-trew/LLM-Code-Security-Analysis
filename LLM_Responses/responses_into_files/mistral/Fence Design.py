import sys
input = sys.stdin.readline

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0 and (q[0] - p[0]) * (r[1] - q[1]) == (r[0] - q[0]) * (q[1] - p[1]):
        return 0
    elif val > 0:
        return 1
    else:
        return -1

def max_fences(poles, fences):
    n = len(poles)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if orientation(poles[i], poles[j], poles[(i+1) % n]) == -1 and \
               orientation(poles[i], poles[j], poles[(j+1) % n]) == 1:
                edges.append((i+1, j+1))

    fences_count = len(fences)
    max_fences = fences_count

    for i in range(len(edges)):
        edge = edges[i]
        for j in range(i + 1, len(edges)):
            other_edge = edges[j]
            if orientation(poles[edge[0]-1], poles[edge[1]-1], poles[other_edge[0]-1]) == -1 and \
               orientation(poles[other_edge[0]-1], poles[other_edge[1]-1], poles[edge[0]-1]) == 1:
                edges[i] = (min(edge), max(edge))
                edges[j] = (min(other_edge), max(other_edge))
                max_fences += 1

    return max_fences - fences_count

T = int(input())
for t in range(1, T+1):
    n = int(input())
    poles = [list(map(int, input().split())) for _ in range(n)]
    fences = []
    for _ in range(2):
        p, q = map(int, input().split())
        fences.append((p-1, q-1))
    print("Case #{}: {}".format(t, max_fences(poles, fences)))
    additional_fences = max_fences(poles, fences)
    for _ in range(additional_fences):
        print(*max([(i+1, j+1) for i,j in edges if (i not in [p, q] and j not in [p,q])], key=lambda x:x[0] * n + x[1]))


This code reads the number of test cases, then iterates over each test case. For each test case, it first calculates all possible edges between poles that form a valid fence (i.e., the two points are not collinear with any other point). Then it checks if adding new fences created from these edges would result in intersecting fences. If not, it adds the new fence and increments the count of additional fences. Finally, it outputs the number of additional fences that can be added and their corresponding poles.