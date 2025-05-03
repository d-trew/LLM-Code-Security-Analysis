T = int(input())
for _ in range(T):
    N = int(input())
    weights = list(map(int, input().split()))
    stack = []
    for weight in reversed(weights):
        if sum([weight * 6 for weight in stack]) >= weight:
            stack.append(weight)
    print(f"Case #{_+1}: {len(stack)}")