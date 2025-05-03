import sys
from random import randint

def find_order(n, q):
    # Generate T} lists of n elements randomly
    lists = [sorted([randint(1, 2*n) for _ in range(n)] for i in range(t)]
    
    # Process each test case
    for i in range(t):
        # Initialize the list to be sorted
        unsorted_list = lists[i]
        
        # Keep track of the current order, assume it is not reversed
        order = [x-1 for x in range(n+1)]
        
        # Track how many questions have been asked so far
        num_questions_asked = 0
        
        while num_questions_asked < q:
            # Pick three distinct indices to compare
            a, b, c = randint(1, n), randint(1, n), randint(1, n)
            while (a == b or a == c or b == c):
                a, b, c = randint(1, n), randint(1, n), randint(1, n)
            
            # Ask the judge for the median of these three elements
            print(f"{a} {b} {c}")
            sys.stdout.flush()
            answer = int(input())
            
            if answer == -1:
                break
            num_questions_asked += 1
            
            # Update the order of the elements based on the response
            if a == answer or b == answer:
                order[a], order[b] = b, a
            else:
                order[c] = n-1
        
        # Sort the remaining elements using the updated order
        sorted_list = [unsorted_list[order.index(x)] for x in range(n)]
        
        # Print the final answer and wait for judge's response
        print(" ".join([str(x) for x in sorted_list]))
        sys.stdout.flush()
        result = int(input())
        
        if result == -1:
            break
    
    return

# Read input from the testing tool
t, n, q = map(int, input().split())
find_order(n, q*t)