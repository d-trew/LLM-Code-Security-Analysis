def min_cost_to_retile(R, C, F, S, current_state, target_state):
    diff = 0
    for i in range(R):
        for j in range(C):
            if current_state[i][j] != target_state[i][j]:
                diff += 1
    flips_needed = (diff + 1) // 2
    swaps_needed = max(0, diff - flips_needed * 2)
    return F * flips_needed + S * swaps_needed

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    for _ in range(T):
        R = int(data[index])
        C = int(data[index + 1])
        F = int(data[index + 2])
        S = int(data[index + 3])
        index += 4
        
        current_state = []
        target_state = []
        for i in range(R):
            current_state.append(data[index])
            index += 1
        for i in range(R):
            target_state.append(data[index])
            index += 1
        
        result = min_cost_to_retile(R, C, F, S, current_state, target_state)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i + 1}: {result}")

if __name__ == "__main__":
    solve()