def count_valid_orderings(molecules):
    n = len(molecules)
    if n == 2:
        return 2
    
    valid_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            c1, j1 = molecules[i]
            c2, j2 = molecules[j]
            
            # Check if (i, j) is a valid pair
            if (c1 * j2 > c2 * j1 and c1 * j2 != c2 * j1) or (c1 * j2 < c2 * j1 and c1 * j2 != c2 * j1):
                valid_count += 1
    
    return valid_count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        molecules = []
        index += 1
        
        for _ in range(N):
            Ci, Ji = map(int, data[index:index + 2])
            molecules.append((Ci, Ji))
            index += 2
        
        results.append(count_valid_orderings(molecules))
    
    for i, result in enumerate(results, start=1):
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()