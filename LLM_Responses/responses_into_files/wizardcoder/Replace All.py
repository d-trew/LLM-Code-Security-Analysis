import sys

def main():
    T = int(input())
    for i in range(T):
        S, N = input(), int(input())
        replacements = [tuple(map(str, input().split())) for _ in range(N)]
        max_chars = 0
        
        for p1, p2 in replacements:
            max_chars += len([c for c in S if c not in p1]) + 1
            S = S.replace(p1, p2)
            
        print("Case #{}: {}".format(i+1, max_chars))
        
if __name__ == "__main__":
    main()