import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    for _ in range(T):
        Nmax = int(data[index])
        M = int(data[index + 1])
        R = int(data[index + 2])
        index += 3
        
        def query(A, B):
            print(f"{A} {B}")
            sys.stdout.flush()
            return int(input())
        
        def response(C, D):
            print(f"{C} {D}")
            sys.stdout.flush()
            
        # Phase 1: Querying the judge
        for _ in range(R):
            A = B = 0  # Placeholder values, actual logic needed here
            total_moves = query(A, B)
        
        # Phase 2: Responding to the judge's requests
        for _ in range(R):
            C = D = 0  # Placeholder values, actual logic needed here
            response(C, D)
    
if __name__ == "__main__":
    main()