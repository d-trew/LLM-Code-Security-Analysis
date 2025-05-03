import sys
from heapq import heappop, heappush

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        r, b, c = map(int, sys.stdin.readline().split())
        cashiers = [list(map(int, sys.stdin.readline().split())) for _ in range(c)]

        robots = sorted([(m, i) for i, (m, _, _) in enumerate(cashiers)] + \
                       [(b, i) for i, (_, s, _) in enumerate(cashiers) if m >= b])
        total_time = 0

        heap = []
        for robot, bits in robots:
            heappush(heap, (bits * sum([s for _, s, _ in cashiers[robot]], 0), robot))

        while heap:
            time, robot = heappop(heap)
            if not len(cashiers[robot]):
                continue
            cashier = cashiers[robot].pop(0)
            total_time += cashier[1] + cashier[2]

        print("Case #{}: {}".format(_ + 1, total_time))

solve()