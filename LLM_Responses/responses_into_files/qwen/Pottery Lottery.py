import sys

def read_input():
    return int(sys.stdin.readline().strip())

def write_output(V, P):
    print(f"{V} {P}", flush=True)

T = read_input()
for _ in range(T):
    day = read_input()
    if day == 100:
        V = 20
        P = 100
    else:
        V = min(day // 10 + 1, 20)
        P = 0
    write_output(V, P)