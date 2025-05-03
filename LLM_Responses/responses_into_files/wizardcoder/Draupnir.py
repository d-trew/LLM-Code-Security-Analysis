import sys

def get_input():
    return int(sys.stdin.readline().strip())

def main():
    T = get_input()
    W = get_input()
    for i in range(T):
        rings = [0] * 6
        days = [0] * (51)
        
        for j in range(W+1):
            guess = input().split(' ')
            
            if len(guess) == 1 and int(guess[0]) == -1:
                break
                
            for k, val in enumerate(guess):
                rings[k] += int(val) % 263
                
            days[j+1] = sum([rings[l] for l in range(6)]) % 263
            
        print(*rings)
        
if __name__ == "__main__":
    main()