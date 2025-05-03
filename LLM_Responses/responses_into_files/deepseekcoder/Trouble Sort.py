def trouble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        if i % 3 == 0:
            for j in range(0, n - i//3 - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
        else:
            for j in range(n - i//3 - 1, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    swapped = True
        if not swapped:
            return i+1
    return "OK"

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    V = list(map(int, input().split()))
    result = trouble_sort(V)
    if isinstance(result, str):
        print("Case #{}: {}".format(t, "OK"))
    else:
        print("Case #{}: {}".format(t, result))