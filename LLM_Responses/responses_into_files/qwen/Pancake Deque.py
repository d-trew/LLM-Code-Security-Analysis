from collections import deque

def max_customers_paid(N, D):
    left = deque(D)
    right = deque(D[::-1])
    result = 0
    
    while left:
        if not right or (left and left[0] >= right[0]):
            if left[0] >= result:
                result += 1
            left.popleft()
        else:
            if right[0] >= result:
                result += 1
            right.popleft()
    
    return result

T = int(input())
results = []

for i in range(1, T + 1):
    N = int(input())
    D = list(map(int, input().split()))
    results.append(max_customers_paid(N, D))

for i, result in enumerate(results, start=1):
    print(f"Case #{i}: {result}")