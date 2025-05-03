import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        A = int(data[index])
        B = int(data[index + 1])
        N = int(data[index + 2])
        index += 3
        
        left, right = A + 1, B
        attempts = 0
        
        while attempts < N:
            guess = (left + right) // 2
            print(guess)
            sys.stdout.flush()
            
            response = input().strip()
            
            if response == "WRONG_ANSWER":
                results.append("WRONG_ANSWER")
                break
            
            attempts += 1
            
            if response == "CORRECT":
                results.append("CORRECT")
                break
            elif response == "TOO_SMALL":
                left = guess + 1
            else:  # TOO_BIG
                right = guess - 1
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()