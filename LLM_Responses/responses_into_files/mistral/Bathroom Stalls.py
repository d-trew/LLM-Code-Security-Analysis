import sys
input = sys.stdin.readlines

def max_min_dist(n, k):
    occupied = [False] * (n + 2)
    occupied[0], occupied[n+1] = True, True

    for i in range(1, n+1):
        if not occupied[i]:
            left = right = float('inf')
            for j in range(max(0, i-k), i):
                if j < 0: continue
                left = min(left, i - j)
                if occupied[j]: break
            for j in range(i+1, min(n+2, i+k+1)):
                if j > n+1: break
                right = min(right, j - i)
                if occupied[j]: break

            if left == right:
                occupied[i] = True
                break
            elif left > right:
                occupied[i-right] = True

    return max(max_dist := [(i, max(left, right)) for i, (left, right) in enumerate(zip(*[(occupied.index(False), *maxminDist(n, k-1)) for _ in range(k)]))]), min_dist := [(i, min(left, right)) for i, (left, right) in enumerate(zip(*[(occupied.index(False), *maxminDist(n, k-1)) for _ in range(k)]))])[-1]

T = int(input()[0].strip())
for case_num, (n, k) in enumerate(map(int, input()), 1):
    max_dist, min_dist = max_min_dist(n, k)
    print(f"Case #{case_num}: {max_dist[0]} {min_dist[0]}")


This Python code reads the number of test cases from the standard input (stdin), then iterates through each case and calculates the maximum and minimum distances for the last person entering the bathroom based on the given rules. The function `max_min_dist(n, k)` recursively computes the left and right distances for all empty stalls, taking into account the current number of people (k) and the total number of stalls (n). It then returns the maximum and minimum distance tuple for the last person to enter the bathroom. The main function iterates through the test cases, calculating the max and min distances for each case, and printing the result in the expected format.