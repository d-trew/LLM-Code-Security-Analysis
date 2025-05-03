import sys
from random import randint

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    W = int(data[index + 1])
    index += 2
    
    for _ in range(T):
        P = int(data[index])
        index += 1
        
        if P == -1:
            sys.exit(1)
        
        if P == -3:
            break
        
        Q = randint(P, min(P + 9, 50))
        print(Q)
        sys.stdout.flush()

if __name__ == "__main__":
    main()