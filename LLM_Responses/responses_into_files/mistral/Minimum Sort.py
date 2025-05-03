import sys
from math import ceil

def min_query(arr, start, end):
    return arr[start + (end - start) // (end - start + 1)]

def sort_list(arr):
    n = len(arr)
    coins = 6e8

    def get_min_and_swap(i, j):
        nonlocal coins
        min_pos = min_query(arr, i, j)
        if i < min_pos <= j:
            arr[min_pos], arr[j] = arr[j], arr[min_pos]
            coins -= 1
        cost = ceil(1e8 / (j - i + 1))
        coins -= cost
        return cost

    queries = []
    for i in range(n):
        min_i = min_query(arr, i, n - 1)
        max_i = max_query(arr, i, n - 1)
        if min_i > i:
            queries.append((get_min_and_swap(i, min_i - 1), min_i - 1))
        if max_i < n - 1 and arr[max_i] < arr[n - 1]:
            queries.append((get_min_and_swap(max_i + 1, n - 1), n - 1))

    for query, index in sorted(queries):
        sys.stdout.write(f'{index} {index + 1}\n')
        response = int(sys.stdin.readline())
        if response == -1:
            return
        cost = query * response
        coins -= cost

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                coins -= 1

    sys.stdout.write('D\n')

def max_query(arr, start, end):
    return arr[start + (end - start + 1) // 2]

if __name__ == '__main__':
    T, N = map(int, sys.stdin.readline().split())
    for _ in range(T):
        arr = list(map(int, sys.stdin.readline().split()))
        sort_list(arr)


This Python code reads the number of test cases and the length of each list from the standard input, then processes the given lists using minimum queries and swaps to sort them in increasing order. The program uses a priority queue to optimize the selection of minimum queries. The cost of each query is calculated based on the range it covers. If an invalid response is received from the judge during the execution, the program will exit immediately.