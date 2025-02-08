import math

def query_min(l, r):
    print(f"M {l} {r}")
    response = int(input())
    if response == -1:
        exit()
    return response

def sort_list(n):
    arr = list(range(1, n + 1))
    budget = 6 * 10**8
    
    for i in range(n):
        min_index = query_min(i + 1, n)
        if min_index != i + 1:
            print(f"S {min_index} {i + 1}")
            response = int(input())
            if response == -1:
                exit()

T, N = map(int, input().split())

for _ in range(T):
    sort_list(N)
    print("D")
    response = int(input())
    if response == -1:
        exit()