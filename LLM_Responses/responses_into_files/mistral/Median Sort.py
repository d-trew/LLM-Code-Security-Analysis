import sys
from heapq import heappush, heappop

def find_median(n, queries):
    medians = [None] * n
    min_heap = []
    for i in range(1, n+1):
        heappush(min_heap, i)

    for i, j, k in queries:
        x = heappop(min_heap)
        y = heappop(min_heap)
        z = heappop(min_heap)
        heappush(min_heap, x)
        heappush(min_heap, y)
        if len(min_heap) == 0:
            medians[i-1] = (z + min(x, y)) // 2
        elif len(min_heap) == 1:
            medians[i-1] = heappop(min_heap)
        else:
            m = heappop(min_heap)
            medians[i-1] = m if (len(min_heap) % 2 == 0 and min(x, y, k) <= m <= max(x, y, k)) or (len(min_heap) % 2 != 0 and m < x and m > y) else None
            heappush(min_heap, m)

    sorted_indices = sorted([i for i, _ in enumerate(medians) if medians[i] is not None])
    return [sorted_indices[i] + 1 for i in range(len(sorted_indices))]

if __name__ == "__main__":
    T = int(input().split()[0])
    for _ in range(T):
        n, q, queries = map(int, input().split())
        result = find_median(n, [list(map(int, line.split())) for _ in range(q)] )
        print(' '.join(str(i) for i in result))


This Python program reads the number of test cases T, and for each test case it processes the given number of queries using median questions to find out the order of the N elements. The program then prints the sorted or reverse sorted indices of the elements.