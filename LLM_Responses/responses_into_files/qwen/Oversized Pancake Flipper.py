def min_flips(s, k):
    n = len(s)
    flips = 0
    i = 0
    while i < n:
        if s[i] == '-':
            if i + k > n:
                return "IMPOSSIBLE"
            else:
                flips += 1
                for j in range(i, i + k):
                    s = s[:j] + ('+' if s[j] == '-' else '-') + s[j+1:]
        i += 1
    return flips

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    index = 1
    
    for _ in range(t):
        s = data[index]
        k = int(data[index + 1])
        result = min_flips(s, k)
        results.append(result)
        index += 2
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    main()