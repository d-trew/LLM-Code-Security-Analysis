import sys

def alchemy_spell(N, A, B, U):
    if max(U) < N:
        return "IMPOSSIBLE"
    
    for i in range(1, N+1):
        if sum([u for u in U if u >= i]) > 0 and (i - A) <= 0:
            continue
        elif sum([u for u in U if u >= i]) < 0:
            return "IMPOSSIBLE"
        else:
            return i

def main():
    T = int(input())
    
    for t in range(1, T+1):
        N, A, B = map(int, input().split())
        U = list(map(int, input().split()))
        
        result = alchemy_spell(N, A, B, U)
        
        print("Case #{}: {}".format(t, result))
    
if __name__ == "__main__":
    main()