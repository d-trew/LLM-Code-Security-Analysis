import sys

def read_input():
    return int(sys.stdin.readline().strip())

def write_output(x, y):
    print(f"{x} {y}")
    sys.stdout.flush()

def main():
    T = read_input()
    for _ in range(T):
        A = read_input()
        prepared = set()
        
        while True:
            if len(prepared) >= A:
                break
            
            i, j = 2 + (len(prepared) % 987), 2 + (len(prepared) // 987)
            write_output(i, j)
            
            x, y = map(int, sys.stdin.readline().strip().split())
            if x == -1 and y == -1:
                break
            
            prepared.add((x, y))

if __name__ == "__main__":
    main()