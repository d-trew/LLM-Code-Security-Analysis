import heapq

def solve(n, c, balls):
    # Initialize variables
    power = 0
    heap = []
    pos = 0
    
    # Sort the balls by position and add them to the heap
    for x, s in sorted((x, s) for x, s in balls if x != 0):
        while pos < x:
            if not heap or (heap[0][1] == 1 and c > 0):
                power += min(c, abs(pos - x))
                c = 0
            else:
                power += abs(pos - x) + heapq.heappop(heap)[0]
            pos = x
        if s == 0:
            heapq.heappush(heap, (abs(x), 0))
        elif not heap or heap[0][1] == s:
            heapq.heappush(heap, (abs(x) + 1, s))
        else:
            power += abs(pos - x) + heapq<｜begin▁of▁sentence｜>.pop()[0]
            pos = x
    # Handle remaining balls in the heap
    while heap:
        if not heap or (heap[0][1] == 1 and c > 0):
            power += min(c, abs(pos - 0))
            c = 0
        else:
            power += abs(pos + 0) + heapq.heappop(heap)[0]
    return power

T = int(input())
for case in range(1, T+1):
    N, C = map(int, input().split())
    balls = [tuple(map(int, input().split())) for _ in range(N)]
    print("Case #{}: {}".format(case, solve(N, C, balls)))