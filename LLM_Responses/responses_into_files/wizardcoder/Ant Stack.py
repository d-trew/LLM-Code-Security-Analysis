import sys
from collections import deque

def main():
    T = int(input())
    
    for i in range(1, T+1):
        N = int(input())
        W = list(map(int, input().split()))
        
        stack_lengths = [0] * N
        max_stack_length = 0
        for j in range(N-1, -1, -1):
            if W[j] <= (6*W[max_stack_length] + 24) and j > 0:
                stack_lengths[j] = stack_lengths[max_stack_length]+1
                max_stack_length = j
        
        print("Case #%d: %d" % (i, max_stack_length+1))
    
if __name__ == "__main__":
    main()