import sys

def get_napkin(vertices):
    return {vertex[0]: vertex[1] for vertex in vertices}

def get_folding_patterns(napkin, k):
    patterns = []
    for i in range(k-1):
        pattern = []
        for j in range(i+1, len(napkin)):
            if napkin[j][0] == napkin[i][0]:
                pattern.append((napkin[i][1], napkin[j][1]))
            elif napkin[j][0] == napkin[i][0]+1:
                pattern.append((napkin[i][1], napkin[j][1]+1))
        patterns.append(pattern)
    return patterns

def is_neat_folding_pattern(pattern, k):
    for i in range(k-1):
        if not (0 <= pattern[i][0] < pattern[i][1] < 2*pattern[i][0]+1 and 0 <= pattern[i+1][0] < pattern[i+1][1] < 2*pattern[i+1][0]+1):
            return False
    for i in range(k-1):
        if not (pattern[i][0] == pattern[i+1][0] or pattern[i][0]+1 == pattern[i+1][0]):
            return False
    for i in range(k-2):
        for j in range(i+1, k-1):
            if (pattern[i][0] <= pattern[j][0] < pattern[j][1] < pattern[i][1]) or (pattern[i][0]+1 <= pattern[j][0] < pattern[j][1] < pattern[i][1]+1):
                return False
    return True

def get_neat_folding_patterns(napkin, k):
    patterns = []
    for i in range(k-1):
        pattern = []
        for j in range(i+1, len(napkin)):
            if napkin[j][0] == napkin[i][0]:
                pattern.append((napkin[i][1], napkin[j][1]))
            elif napkin[j][0] == napkin[i][0]+1:
                pattern.append((napkin[i][1], napkin[j][1]+1))
        if is_neat_folding_pattern(pattern, k):
            patterns.append(pattern)
    return patterns

def solve(test_case):
    N, K = test_case
    vertices = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        vertices.append((x, y))
    napkin = get_napkin(vertices)
    if K == 2:
        patterns = get_folding_patterns(napkin, K)
        for pattern in patterns:
            print("Case #1: POSSIBLE")
            for segment in pattern:
                print(f"{segment[0]}/{segment[1]} {segment[2]}/{segment[3]}")
    else:
        patterns = get_neat_folding_patterns(napkin, K)
        if len(patterns) > 0:
            print("Case #1: POSSIBLE")
            for pattern in patterns:
                for segment in pattern:
                    print(f"{segment[0]}/{segment[1]} {segment[2]}/{segment[3]}")
        else:
            print("Case #1: IMPOSSIBLE")