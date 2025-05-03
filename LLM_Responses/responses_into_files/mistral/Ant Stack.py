import sys
input = sys.stdin.readlines

def solve(ants):
    weights = [int(w) for w in ants[1].split()]
    n = len(weights)
    if n == 1:
        return 1
    max_weight = max(weights)
    max_stack_height = 0
    for i in range(n - 1, -1, -1):
        if weights[i] <= (max_weight * 6):
            max_stack_height += 1
            max_weight -= weights[i]
    return max_stack_height + 1

T = int(input()[0])
for case in range(1, T+1):
    ants = input()
    print("Case #{}: {}".format(case, solve(ants)))