def min_time_to_finish(R, B, C, cashiers):
    cashiers.sort(key=lambda x: x[0], reverse=True)
    total_time = 0
    for i in range(R):
        if i < B:
            bits = 1
        else:
            bits = (B - i + R - 1) // (R - i)
        total_time = max(total_time, bits * cashiers[i][1] + cashiers[i][2])
    return total_time

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        R = int(data[index])
        B = int(data[index + 1])
        C = int(data[index + 2])
        cashiers = []
        index += 3
        
        for _ in range(C):
            Mi = int(data[index])
            Si = int(data[index + 1])
            Pi = int(data[index + 2])
            cashiers.append((Mi, Si, Pi))
            index += 3
        
        results.append(min_time_to_finish(R, B, C, cashiers))
    
    for i, result in enumerate(results):
        print(f"Case #{i + 1}: {result}")

if __name__ == "__main__":
    main()