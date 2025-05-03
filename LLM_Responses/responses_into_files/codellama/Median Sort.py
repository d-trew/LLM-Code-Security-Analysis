import sys

# Read input from stdin
T = int(input())
for t in range(T):
    N, Q = map(int, input().split())
    # Initialize a list to store the indices of the elements in sorted order
    sorted_indices = []
    for q in range(Q):
        i, j, k = map(int, input().split())
        # Find the median of the set {x_i, x_j, x_k}
        if (i == j) or (j == k) or (i == k):
            # If any two elements are equal, the other element is the median
            median = i
        else:
            # Otherwise, find the element that is neither the minimum nor the maximum among the three
            if x_i < x_j and x_i < x_k:
                median = i
            elif x_j < x_i and x_j < x_k:
                median = j
            else:
                median = k
        # Print the index of the median element
        print(median)
        # Read the answer from stdin
        answer = int(input())
        if answer == -1:
            break
        # If the answer is correct, add the indices of the elements in sorted order to the list
        elif answer == 1:
            sorted_indices.extend([i, j, k])
    # Sort the list of indices in ascending order
    sorted_indices.sort()
    # Print the indices of the elements in sorted order
    print(*sorted_indices)