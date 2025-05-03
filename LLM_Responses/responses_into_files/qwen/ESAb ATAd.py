import sys

# Read input from stdin
input = sys.stdin.read
data = input().split()

# Parse the first line for T and B
T = int(data[0])
B = int(data[1])

# Initialize index for reading the bit positions
index = 2

# Function to make a query
def query(bit_position):
    print(bit_position, flush=True)
    return int(input())

# Function to exchange the bits
def exchange(bits):
    print(' '.join(map(str, bits)), flush=True)

# Process each test case
for _ in range(T):
    # Initialize the array with -1 (unknown bits)
    array = [-1] * B
    
    # Make up to 150 queries
    for i in range(B):
        if array[i] == -1:
            array[i] = query(i + 1)
    
    # Exchange the bits
    exchange(array)

# The program will automatically exit after the last exchange