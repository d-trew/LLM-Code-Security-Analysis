import sys
from collections import defaultdict
from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def solve():
    input = sys.stdin.readline().strip()
    N = int(input)
    jugglers = []
    for _ in range(N * 2):
        x, y = map(int, sys.stdin.readline().strip().split())
        jugglers.append((x, y))
    
    # Sort the jugglers by their x-coordinates
    jugglers.sort()
    
    pairs = defaultdict(list)
    for i in range(N * 2):
        if len(pairs[jugglers[i][1]]) < N:
            # Find the nearest neighbor to the right that has not been paired yet
            for j in range(i + 1, N * 2):
                if jugglers[j][1] == jugglers[i][1]:
                    pairs[jugglers[i][1]].append((jugglers[i][0], jugglers[j][0]))
                    break
    
    # Sort the pairs by their y-coordinates
    for key in pairs.keys():
        pairs[key].sort(reverse=True)
        
    result = []
    for i in range(N * 2):
        if jugglers[i][1] in pairs:
            pair = pairs[jugglers[i][1]].pop()
            result.append((jugglers[i][0], pair[1]))
            
    return result

T = int(sys.stdin.readline().strip())
for t in range(1, T + 1):
    pairs = solve()
    print('Case #{}:'.format(t), end=' ')
    for pair in pairs:
        print(*pair, end=' ')
    print()