def max_stack_ants(N, weights):
    stack = []
    for weight in weights:
        while stack and weight > stack[-1] * 6:
            stack.pop()
        if not stack or weight <= stack[-1]:
            stack.append(weight)
    return len(stack)

T = int(input())
results = []
for i in range(1, T + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    results.append(f"Case #{i}: {max_stack_ants(N, weights)}")

for result in results:
    print(result)