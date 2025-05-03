def min_operations(exercises, weights):
    total_operations = 0
    current_stack = [0] * (weights + 1)
    
    for exercise in exercises:
        required_weights = exercise[:]
        operations = 0
        
        for i in range(1, weights + 1):
            if required_weights[i - 1] > current_stack[i]:
                operations += (required_weights[i - 1] - current_stack[i])
                current_stack[i] = required_weights[i - 1]
        
        total_operations += operations
    
    return total_operations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        E = int(data[index])
        W = int(data[index + 1])
        index += 2
        
        exercises = []
        
        for _ in range(E):
            exercise = [0] * (W + 1)
            for j in range(W):
                Xij = int(data[index])
                exercise[j + 1] = Xij
                index += 1
            exercises.append(exercise)
        
        result = min_operations(exercises, W)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i + 1}: {result}")

if __name__ == "__main__":
    main()