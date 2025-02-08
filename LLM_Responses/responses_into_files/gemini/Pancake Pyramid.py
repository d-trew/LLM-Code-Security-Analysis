def solve():
    S = int(input())
    P = list(map(int, input().split()))
    MOD = 1000000007

    total_cost = 0
    for L in range(S - 2):
        for R in range(S - 2 - L):
            remaining_stacks = P[L:S - R]
            n = len(remaining_stacks)
            
            min_cost = float('inf')
            for j in range(1, n + 1):
                cost = 0
                temp_stacks = list(remaining_stacks)
                
                #Make it increasing till j
                for i in range(j - 1):
                    if temp_stacks[i+1] < temp_stacks[i]:
                        cost += temp_stacks[i] - temp_stacks[i+1]
                        temp_stacks[i+1] = temp_stacks[i]

                #Make it decreasing from j
                for i in range(j,n):
                    if temp_stacks[i-1] < temp_stacks[i]:
                        cost += temp_stacks[i] - temp_stacks[i-1]
                        temp_stacks[i-1] = temp_stacks[i]

                min_cost = min(min_cost, cost)

            total_cost = (total_cost + min_cost) % MOD

    return total_cost

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")