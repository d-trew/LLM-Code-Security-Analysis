def solve_fractal_artwork(K, C, S):
    if K == 1:
        return [1]
    
    if K <= S:
        return list(range(1, K + 1))
    
    if (K - 1) * (2 ** (C - 1)) < S:
        return "IMPOSSIBLE"
    
    tiles_to_clean = []
    for i in range(S):
        tile_position = (i + 1) * ((K - 1) // (2 ** (C - 1)))
        tiles_to_clean.append(tile_position)
    
    return tiles_to_clean

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        K = int(data[index])
        C = int(data[index + 1])
        S = int(data[index + 2])
        index += 3
        
        result = solve_fractal_artwork(K, C, S)
        if isinstance(result, str):
            results.append(f"Case #{_ + 1}: {result}")
        else:
            results.append(f"Case #{_ + 1}: {' '.join(map(str, result))}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()