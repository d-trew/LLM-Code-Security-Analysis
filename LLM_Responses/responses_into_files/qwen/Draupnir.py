import sys

def query(day):
    print(f"Q {day}")
    sys.stdout.flush()
    return int(input())

def main():
    T, W = map(int, input().split())
    
    for _ in range(T):
        R = [0] * 7
        
        # Make initial guesses based on the constraints
        for i in range(1, 7):
            R[i] = query(0)
        
        # Use the well of knowledge up to W times
        for _ in range(W):
            day = int(input())
            if day == -1:
                break
            
            count = [0] * 7
            for i in range(1, 7):
                count[i] = query(day)
            
            # Update the R values based on the counts
            for i in range(1, 7):
                R[i] += count[i]
        
        # Output the final R values modulo 263
        print("A")
        for r in R[1:]:
            print(f"{r} ", end="")
        print()
        sys.stdout.flush()

if __name__ == "__main__":
    main()