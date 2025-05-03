import sys
T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    gophers = list(map(int, sys.stdin.readline().split()))
    print(len(set(gophers)))