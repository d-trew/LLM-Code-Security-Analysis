MOD = 1000000007

def solve():
    N = int(input())
    V = list(map(int, input().split()))

    count = 0
    
    import itertools
    for perm in itertools.permutations(range(1, N + 1)):
        visible = []
        stack = []
        for i in range(N):
            stack.append(perm[i])
            vis = 1
            largest = stack[-1]
            for j in range(len(stack) - 2, -1, -1):
                if stack[j] > largest:
                    break
                vis += 1
                largest = stack[j]
            visible.append(vis)
        if visible == V:
            count += 1

    return count % MOD

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")