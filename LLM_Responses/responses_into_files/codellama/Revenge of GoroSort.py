import sys

T, N, K = map(int, sys.stdin.readline().split())

# Read the initial array of integers from stdin
arr = list(map(int, sys.stdin.readline().split()))

# Create a dictionary to store the frequency of each integer in the array
freq = {}
for i in arr:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

# Create an array to store the sorted integers
sorted_arr = []

# While there are still integers in the array that have not been sorted
while len(sorted_arr) < N:

    # Find the integer with the highest frequency and add it to the sorted array
    max_freq = 0
    for i in freq:
        if freq[i] > max_freq:
            max_freq = freq[i]
            max_val = i

    sorted_arr.append(max_val)

    # Decrement the frequency of the integer that was added to the sorted array
    freq[max_val] -= 1

# Print the final sorted array
print(' '.join(map(str, sorted_arr)))