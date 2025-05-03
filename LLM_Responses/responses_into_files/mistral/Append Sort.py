import sys
from itertools import accumulate

def min_append(nums):
    nums = sorted(nums)
    total = sum(nums) + len(nums) - 1
    return total - sum(accumulate(nums))

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    nums = sorted(list(map(int, sys.stdin.readline().split())))
    print(f"Case #{_ + 1}: {min_append(nums)}")


This program reads the number of test cases from stdin and then iterates through each test case. For each test case, it reads the number of integers in the list and the list itself, sorts the list, calculates the minimum number of single digit append operations needed to make the list strictly increasing using the `min_append()` function, and finally prints the result. The `min_append()` function calculates the total number of digits required for the sorted list and subtracts the sum of the cumulative sum of the original list to get the minimum number of single digit append operations needed.