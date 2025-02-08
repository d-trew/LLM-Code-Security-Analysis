def trouble_sort(nums):
    n = len(nums)
    sorted_nums = nums[:]
    sorted_nums.sort()
    
    while True:
        swapped = False
        for i in range(n - 2):
            if nums[i] > nums[i+2]:
                nums[i], nums[i+1], nums[i+2] = nums[i+2], nums[i+1], nums[i]
                swapped = True
        if not swapped:
            break

    for i in range(n - 1):
        if nums[i] > nums[i+1]:
            return i
    return "OK"

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    result = trouble_sort(nums)
    print(f"Case #{i}: {result}")