import random
from collections import defaultdict

def main():
    T = int(input())
    
    for test in range(T):
        B, N = map(int, input().split())
        
        # initialize the array with 0's
        arr = [0] * B
        
        # keep track of queries and fluctuations
        query_count = defaultdict(int)
        fluctuation_count = defaultdict(int)
        
        for i in range(N):
            # make a random query between 1 and B (inclusive)
            pos = random.randint(1, B)
            
            # increment the count of queries at this position
            query_count[pos] += 1
            
            # check if it's time for a fluctuation
            if i + 1 in [j * (j+10) for j in range(1, 15)]:
                fluc = random.randint(1,4)
                
                # increment the count of fluctuations at this position
                fluctuation_count[pos] += fluc
                
                if fluc == 3:
                    arr[pos-1] = not arr[pos-1]
        
        print(" ".join(map(str, arr))

if __name__ == "__main__":
    main()

# this is just a starting point; you should add more test cases and optimize the algorithm to find the entire array