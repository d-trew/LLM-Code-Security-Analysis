import sys
from collections import Counter

def count_digits(n):
    digits = [0] * 10
    i = 1
    while True:
        for digit in str(i*n):
            if int(digit) not in digits:
                digits[int(digit)] += 1
            if all(digits):
                return i*n
            i += 1

def main():
    T = int(input())
    
    for tc in range(T):
        N = int(input())
        
        last_number = count_digits(N)
        
        if last_number == float('inf'):
            print("Case #{}: INSOMNIA".format(tc+1))
        else:
            print("Case #{}: {}".format(tc+1, last_number))
            
if __name__ == "__main__":
    main()