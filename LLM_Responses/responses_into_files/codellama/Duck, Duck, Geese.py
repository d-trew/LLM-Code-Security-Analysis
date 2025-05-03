import sys

def solve(N, C, A, B, P):
    # Initialize a dictionary to store the number of players for each color
    color_count = {i: 0 for i in range(1, C+1)}
    # Update the dictionary with the number of players wearing each color
    for player in P:
        color_count[player] += 1
    
    # Initialize a list to store the valid combinations
    valid_combinations = []
    # Iterate over all possible combinations of geese
    for i in range(N-1, -1, -1):
        # Check if the current combination is valid
        valid = True
        for j in range(1, C+1):
            # If the number of players wearing color j is not between A_j and B_j, invalidate the combination
            if color_count[j] < A[j-1] or color_count[j] > B[j-1]:
                valid = False
                break
        # If the current combination is valid, add it to the list of valid combinations
        if valid:
            valid_combinations.append(i)
    
    return len(valid_combinations)

if __name__ == "__main__":
    T = int(input())
    for case in range(1, T+1):
        N, C = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        P = list(map(int, input().split()))
        print("Case #" + str(case) + ": " + str(solve(N, C, A, B, P)))