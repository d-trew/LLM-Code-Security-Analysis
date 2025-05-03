T = int(input())
for _ in range(T):
    N = int(input())
    arr = [int(x) for x in input().split()]
    low, high = 0, N-1
    while low < high:
        min_idx = (low + high)//2
        if arr[min_idx] > arr[high]:
            high = min_idx
        elif arr[low] > arr[high]:
            low, high = high, low
        else:
            high -= 1
    print(low)