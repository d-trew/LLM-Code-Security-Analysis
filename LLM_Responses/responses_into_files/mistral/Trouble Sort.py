import sys
input = sys.stdin.readline

def trouble_sort(nums):
    for i in range(len(nums) - 2):
        if nums[i] > nums[i+2]:
            nums[i], nums[i+1], nums[i+2] = nums[i+2], nums[i], nums[i+1]
    return nums

T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    sorted_nums = trouble_sort(nums)
    if sorted_nums != sorted(nums):
        index = next((i for i, x in enumerate(sorted_nums[1:]) if x > sorted_nums[i]), None)
        print(f'Case #{_+1}: Error at {index}')
    else:
        print(f'Case #{_+1}: OK')


This program reads the number of test cases, iterates through each test case, sorts a given list using Trouble Sort algorithm, and checks if it is sorted in non-decreasing order. If not, it finds the index of the first error by checking for any element that is greater than its successor in the sorted list.