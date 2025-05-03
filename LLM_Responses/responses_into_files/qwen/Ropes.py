import sys

def read_int():
    return int(sys.stdin.readline())

T = read_int()
N = read_int()
W = read_int()

for _ in range(T):
    for i in range(N):
        A_i = read_int()
        B_i = read_int()
        print(f"{A_i} {B_i}")
        C_i = read_int()
        D_i = read_int()
    
    result = read_int()
    if result == 0:
        sys.exit(-1)