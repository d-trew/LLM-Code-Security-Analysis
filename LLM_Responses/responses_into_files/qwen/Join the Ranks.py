def reorder_deck(R, S):
    operations = []
    for rank in range(1, R + 1):
        start_index = (rank - 1) * S
        end_index = rank * S
        if start_index != 0:
            operations.append((start_index, end_index - start_index))
    return len(operations), operations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        R = int(data[index])
        S = int(data[index + 1])
        index += 2
        
        num_operations, operations = reorder_deck(R, S)
        
        results.append(f"Case #{_+1}: {num_operations}")
        for a, b in operations:
            results.append(f"{a} {b}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()