def find_color(C, M, Y, K):
    for c in range(10**6 + 1):
        for m in range(10**6 - c + 1):
            for y in range(10**6 - c - m + 1):
                k = 10**6 - c - m - y
                if all(c <= Ci and m <= Mi and y <= Yi and k <= Ki for Ci, Mi, Yi, Ki in zip(C, M, Y, K)):
                    return f"{c} {m} {y} {k}"
    return "IMPOSSIBLE"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        C = list(map(int, data[index:index+4]))
        M = list(map(int, data[index+4:index+8]))
        Y = list(map(int, data[index+8:index+12]))
        K = list(map(int, data[index+12:index+16]))
        
        index += 16
        result = find_color(C, M, Y, K)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i + 1}: {result}")

if __name__ == "__main__":
    main()