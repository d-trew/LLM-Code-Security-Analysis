import sys
from collections import deque
def pyramid_cost(pancakes):
    n = len(pancakes)
    total = 0
    for L in range(n):
        pq = deque()
        for i in range(L, n - 1):
            while pq and pq[0][1] <= pancakes[i]:
                pq.popleft()
            if not pq or pq[-1][0] != pancakes[i]:
                pq.append((pancakes[i], i))
        total += n - 1 - i
    return total % (10**6 + 7)

def main():
    T = int(input())
    for case in range(1, T + 1):
        S = int(input())
        pancakes = list(map(int, input().split()))
        print("Case #%d: %d" % (case, pyramid_cost(pancakes))

if __name__ == "__main__":
    main()