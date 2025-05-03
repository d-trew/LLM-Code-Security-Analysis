def find_smallest_metal(N, A, B, U):
    if sum(U) == 0:
        return "IMPOSSIBLE"
    
    for start in range(1, N + 1):
        queue = [start]
        created = set()
        
        while queue:
            current = queue.pop(0)
            if current not in created:
                created.add(current)
                if current >= A and current - A <= N:
                    queue.append(current - A)
                if current >= B and current - B <= N:
                    queue.append(current - B)
        
        if len(created) == sum(U):
            return start
    
    return "IMPOSSIBLE"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        A = int(data[index + 1])
        B = int(data[index + 2])
        U = list(map(int, data[index + 3:index + 3 + N]))
        
        result = find_smallest_metal(N, A, B, U)
        results.append(result)
        
        index += 3 + N
    
    for i, result in enumerate(results):
        print(f"Case #{i + 1}: {result}")

if __name__ == "__main__":
    main()