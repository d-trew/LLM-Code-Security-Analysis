import sys

def main():
    T = int(input())
    
    for i in range(T):
        C_i, M_i, Y_i, K_i = map(int, input().split())
        
        if C_i + M_i + Y_i <= 10**6 and K_i >= 10**6:
            c = 10**6 - (C_i + M_i + Y_i)
            print(f"Case #{i+1}: {c} {M_i} {Y_i} {K_i}")
        else:
            print(f"Case #{i+1}: IMPOSSIBLE")
    
if __name__ == "__main__":
    main()