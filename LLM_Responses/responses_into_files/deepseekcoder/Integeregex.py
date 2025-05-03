Here's a Python code snippet that uses regular expressions to solve your problem:


import re

def count_matches(A, B, R):
    count = 0
    for i in range(A, B+1):
        if re.fullmatch(R, str(i)):
            count += 1
    return count

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    R = input()
    print("Case #{}: {}".format(tc, count_matches(A, B, R)))

In this code, the `count_matches` function takes two integers and a string as arguments. It iterates over all numbers from A to B (inclusive), checks if each number matches the regular expression R using `re.fullmatch()`, and increments a counter for every match. The main part of the script reads the input data, calls the `count_matches` function with appropriate arguments, and prints the result.