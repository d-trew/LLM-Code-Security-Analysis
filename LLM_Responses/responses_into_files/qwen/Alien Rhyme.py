def largest_rhyming_subset(words):
    n = len(words)
    max_size = 0
    
    for i in range(n):
        accented_suffixes = set()
        for j in range(len(words[i])):
            suffix = words[i][j:]
            if suffix not in accented_suffixes:
                accented_suffixes.add(suffix)
        
        if len(accented_suffixes) == 1:
            max_size += 1
    
    return max_size

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        words = data[index + 1:index + N + 1]
        index += N + 1
        
        result = largest_rhyming_subset(words)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    main()