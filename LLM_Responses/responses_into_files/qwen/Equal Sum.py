import sys

def read_int():
    return int(sys.stdin.readline().strip())

T = read_int()

for _ in range(T):
    N = read_int()
    A = [read_int() for _ in range(N)]
    
    B = [read_int() for _ in range(N)]
    
    # Choose the first N/2 elements from A and the rest from B
    chosen = A[:N//2] + B[N:]
    
    print(len(chosen), *chosen)