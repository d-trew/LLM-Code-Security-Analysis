import sys

def reversort(L, C):
    N = len(L)
    if N == 0 or C == 0:
        return L
    
    i = 1
    j = N
    while i < j:
        reverse(L, i, j)
        i += 1
        j -= 1
    
    return L

def reverse(L, i, j):
    for k in range(i, j+1):
        L[k] = L[k-1]
    L[i] = L[j]
    L[j] = temp

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, C = map(int, input().split())
        if reversort(list(range(1, N+1)), C) == []:
            print("IMPOSSIBLE")
        else:
            print(reversort(list(range(1, N+1)), C))