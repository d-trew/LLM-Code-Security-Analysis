import sys

def solution(N, K):
    L = [0] * N
    R = [0] * N
    
    for i in range(1, N):
        L[i] = i - 1
        R[N - i - 1] = i - 1
        
    max_LS = -1
    min_RS = -1
    
    for i in range(K):
        S = int(input())
        if L[S] > max_LS:
            max_LS = L[S]
        if R[S] < min_RS or min_RS == -1:
            min_RS = R[S]
            
    return (max_LS, min_RS)

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        print("Case #" + str(i+1) + ": " + str(solution(N, K)))