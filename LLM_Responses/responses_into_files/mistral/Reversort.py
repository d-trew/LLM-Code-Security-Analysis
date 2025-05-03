import sys

def reversort(arr):
    n = len(arr)
    costs = [0] * n
    for i in range(n - 1, 0, -1):
        j = arr[i] - 1
        costs[j] = max(costs[j], i + 1 - j)
        if i != j:
            arr[:j + 1], arr[i:] = arr[i:], arr[:j + 1]
    return sum(costs)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print("Case #{}: {}".format(_ + 1, reversort(arr)))

This program reads the number of test cases from the standard input and iterates through each test case. For each test case, it first reads the number of elements in the list and then reads the elements themselves. It then computes the cost of executing Reversort on the given list using the pseudocode provided in the description, and prints the result as specified.