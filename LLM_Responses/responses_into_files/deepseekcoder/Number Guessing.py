import sys

def binary_search(low, high):
    print((low + high) // 2)
    sys.stdout.flush()
    response = input().strip()
    
    if response == 'CORRECT':
        return
    elif response == 'TOO_SMALL':
        binary_search(high, high * 2)
    else: # TOO_BIG
        binary_search(low // 2 + 1, low)

def main():
    T = int(input().strip())
    
    for _ in range(T):
        A, B, N = map(int, input().strip().split())
        
        binary_search(A+1, min(B, 2**63-1))

if __name__ == "__main__":
    main()