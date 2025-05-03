import sys

def min_thermometers(K, X, T):
    N = len(X)
    thermometers = []
    
    for i in range(N-1):
        if T[i] != T[i+1]:
            thermometers.append((X[i], T[i]))
        
    return len(thermometers)+1

def main():
    T = int(input())
    
    for i in range(T):
        K, N = map(int, input().split())
        X = list(map(float, input().strip().split()))
        T = list(map(int, input().strip().split()))
        
        print("Case #{}: {}".format(i+1, min_thermometers(K, X, T))

if __name__ == "__main__":
    main()