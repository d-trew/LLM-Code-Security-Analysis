import heapq
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def solve():
    N, R, K = map(int, input().split())
    points = [tuple(map(float, input().split())) for _ in range(N)]
    
    angles = sorted([(i * 360 / (2 * math.pi), d + l) for i, (d, l) in enumerate(points)])
    angles += [(a + 360, d + l) for a, (d, l) in angles[:K]]
    
    heap = []
    for i in range(N):
        x1, y1 = R * math.cos((angles[i][0] - 90) * math.pi / 180), R * math.sin((angles[i][0] - 90) * math.pi / 180)
        for j in range(i + 1, i + K):
            x2, y2 = R * math.cos((angles[j][0] - 90) * math.pi / 180), R * math.sin((angles[j][0] - 90) * math.pi / 180)
            d = distance(x1, y1, x2, y2)
            heapq.heappush(heap, (-d + angles[i][1] + angles[j][1]))
    
    result = [(-heapq.heappop(heap)) for _ in range(K)]
    print('Case #{}: {}'.format(_ + 1, ' '.join(map(str, result))))

T = int(input())
for _ in range(T):
    solve()