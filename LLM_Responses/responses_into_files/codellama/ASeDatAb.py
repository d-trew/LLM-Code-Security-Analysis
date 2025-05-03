import sys

# Read the number of test cases from stdin
T = int(input())

for t in range(T):
    # Initialize the record with a random value
    record = "".join([str(random.randint(0, 1)) for _ in range(8)])
    while True:
        # Output the current value of the record
        print(record)
        
        # Read the number of ones in the updated value from stdout
        N = int(input())
        
        # If the number of ones is 0, set the record to all zeros
        if N == 0:
            record = "0" * 8
            
        # Otherwise, rotate the record by a random amount and XOR it with itself
        else:
            r = random.randint(0, 7)
            rotated_record = record[r:] + record[:r]
            record = bin(int(rotated_record, 2) ^ int(record, 2))[2:]
            
        # Check if the record is now all zeros
        if record == "0" * 8:
            break
        
# Output a final message indicating that all test cases have been processed
print("All test cases have been processed.")