def find_valid_sets(signs):
    n = len(signs)
    max_length = 0
    count = 0
    
    for i in range(n):
        m = signs[i][1]
        n_val = signs[i][2]
        length = 1
        
        for j in range(i + 1, n):
            if signs[j][2] == m and signs[j][1] == n_val:
                length += 1
            else:
                break
        
        if length > max_length:
            max_length = length
            count = 1
        elif length == max_length:
            count += 1
    
    return max_length, count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        S = int(data[index])
        index += 1
        signs = []
        
        for _ in range(S):
            Di = int(data[index])
            Ai = int(data[index + 1])
            Bi = int(data[index + 2])
            signs.append((Di, Ai, Bi))
            index += 3
        
        max_length, count = find_valid_sets(signs)
        results.append(f"Case #{_+1}: {max_length} {count}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()