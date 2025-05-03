# This Python program is based on the provided description of a problem involving a database system with broken workers. The program evaluates the behavior of the TEST_STORE operation and determines which workers are broken using at most F calls to TEST_STORE, where F = 10 for this test set.

# Read input: Number of test cases (T)
T = int(input())

# Process each test case
for i in range(T):
    # Read input: Number of workers (N), Number of broken workers (B), and Maximum number of calls (F)
    N, B, F = map(int, input().split())

    # Initialize variables for the current test case
    num_calls = 0
    broken_workers = []

    # Loop through each call to TEST_STORE
    while num_calls < F:
        # Read input: String of bits (N characters, either '0' or '1')
        bits = input()

        # Increment the number of calls
        num_calls += 1

        # Check if the current call returns only N - B bits
        if len(bits) == N - B:
            # If so, check if all the returned bits are either '0' or '1'
            if all(bit in ['0', '1'] for bit in bits):
                # If yes, add the current worker to the list of broken workers
                broken_workers.append(num_calls - 1)

    # Sort and print the list of broken workers (if any)
    if broken_workers:
        print(*sorted(broken_workers), sep=' ')
    else:
        print('-1')