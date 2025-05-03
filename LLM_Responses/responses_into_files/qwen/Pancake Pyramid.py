MOD = 10**9 + 7

def pyramidification_cost(stacks):
    n = len(stacks)
    min_cost = float('inf')
    
    for j in range(1, n):
        cost = 0
        for i in range(j):
            if stacks[i] > stacks[j]:
                cost += stacks[i] - stacks[j]
        for i in range(j + 1, n):
            if stacks[i] > stacks[j - 1]:
                cost += stacks[j - 1] - stacks[i]
        min_cost = min(min_cost, cost)
    
    return min_cost

def solve():
    T = int(input())
    results = []
    
    for _ in range(T):
        S = int(input())
        stacks = list(map(int, input().split()))
        
        total_cost = 0
        
        for L in range(S - 2):
            for R in range(S - L - 2):
                remaining_stacks = stacks[L + 1:S - R]
                total_cost += pyramidification_cost(remaining_stacks)
        
        results.append(total_cost % MOD)
    
    for i, result in enumerate(results, start=1):
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    solve()