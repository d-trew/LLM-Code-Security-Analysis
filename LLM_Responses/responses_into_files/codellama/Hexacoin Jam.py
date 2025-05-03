import sys

def solve(N, D, S, E, L):
    # Calculate the number of possible assignments to the last two digits
    num_assignments = 16**D - 2*16 + 1
    
    # Initialize the probability of finding a hexacoin as 0
    prob_hexacoin = 0
    
    # Iterate through each possible assignment of the last two digits
    for i in range(num_assignments):
        # Calculate the sum of the values assigned to the last two digits
        sum_last_digits = S[i] + E[i]
        
        # Check if the sum is between S and E, inclusive
        if S <= sum_last_digits <= E:
            # Increment the probability of finding a hexacoin
            prob_hexacoin += 1/num_assignments
    
    return prob_hexacoin

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, D, S, E = map(int, input().split())
        L = list(map(int, input().split()))
        
        # Call the solve function and print the result
        print("Case #{}: {}".format(t+1, solve(N, D, S, E, L)))