import sys

def trouble_sort(lst):
    n = len(lst)
    for i in range(n-2):
        if lst[i] > lst[i+2]:
            return i
    return 'OK'

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    L = [int(x) for x in sys.stdin.readline().split()]
    print(f'Case #{t+1}: {trouble_sort(L)}')