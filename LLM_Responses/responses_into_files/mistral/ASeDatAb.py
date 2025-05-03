import random

def reset_record(n):
    for _ in range(300):
        value = bin(int(input(), 16))[2:].zfill(8)
        n ^= int(value, 2)
        print(value)
        if not n:
            break

T = int(input())
for _ in range(T):
    record = random.choice([bin(x)[2:] for x in range(1, 256)]).zfill(8)
    reset_record(int(record, 2))
    print(int(input()))


This program reads the number of test cases from the input, then iterates over each test case. For each test case, it sets the record to a random value that is not all 0s, initializes the rotation variable `n` to the binary representation of the record, and then enters a loop where it generates a random 8-bit binary string as the value `value`, performs an XOR operation on `n` with the new value, prints the resulting value, and checks if all bits are 0. If so, it breaks out of the loop and moves on to the next test case or the final output. The judge program will send a single line containing the number of ones in the updated value of the record. This program continues until all test cases have been processed.