import sys

T = int(input())
B = int(input())

for i in range(T):
    arr = list(map(int, input().split()))
    queries = []
    for j in range(150):
        queries.append(list(map(int, input().split())))
    queries.append([])
    print(*arr)