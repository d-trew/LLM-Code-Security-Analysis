import sys
from collections import defaultdict

def read_input():
    return tuple(map(int, input().split()) + [None])

def write_output(line):
    print(line)
    sys.stdout.flush()

def main():
    T, Nmax, M, R = read_input()
    for _ in range(T):
        kings = defaultdict(list)
        requests = []
        for i in range(Nmax):
            xi, yi = map(int, input().split())
            kings[xi].append((yi, i))
        
        write_output("READY")
        for _ in range(R):
            a, b = read_input()
            if a == "DONE":
                break
            elif a == "ERROR" or b == "ERROR":
                continue
            
            total_moves = 0
            for xi, yis in kings.items():
                total_moves += max(abs(xi - a), abs(yis[0][0] - b))
                
            write_output(total_moves)
        
        else:
            continue
        break
    
if __name__ == "__main__":
    main()