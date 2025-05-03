def solve_mascot_assignment(N, L, R):
    mascot_count = [0] * N
    for i in range(N):
        if L[i] != -1:
            mascot_count[L[i]] += 1
        if R[i] != -1:
            mascot_count[R[i]] += 1
    
    max_mascot_needed = max(mascot_count)
    if max_mascot_needed > 13:
        return "IMPOSSIBLE"
    
    mascots = list("ACDEHIJKMORST")
    assignment = [''] * N
    used = set()
    
    for i in range(N):
        if L[i] != -1 and R[i] != -1:
            if assignment[L[i]] == '' and assignment[R[i]] == '':
                assignment[L[i]] = mascots[0]
                assignment[R[i]] = mascots[1]
                used.add(mascots[0])
                used.add(mascots[1])
                mascots = mascots[2:]
    
    for i in range(N):
        if L[i] != -1 and assignment[L[i]] == '':
            assignment[L[i]] = assignment[R[i]]
        elif R[i] != -1 and assignment[R[i]] == '':
            assignment[R[i]] = assignment[L[i]]
    
    return ''.join(assignment)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        L = [-1] * N
        R = [-1] * N
        index += 1
        
        for i in range(N):
            L[i] = int(data[index]) - 1
            index += 1
        
        for i in range(N):
            R[i] = int(data[index]) - 1
            index += 1
        
        result = solve_mascot_assignment(N, L, R)
        results.append(result)
    
    for i, result in enumerate(results, 1):
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()