def generate_latin_square(N, K):
    if (N * N - N) % 2 != K % 2:
        return "IMPOSSIBLE"
    
    square = [[0] * N for _ in range(N)]
    trace_values = [i + 1 for i in range(1, N + 1)]
    remaining_values = list(range(1, N + 1))
    
    for i in range(N):
        if K >= N:
            square[i][i] = remaining_values.pop()
            K -= square[i][i]
        else:
            square[i][i] = trace_values.pop()
            remaining_values.remove(square[i][i])
    
    for row in range(N):
        for col in range(row + 1, N):
            if row == col:
                continue
            while True:
                value = remaining_values.pop(0)
                if value not in square[row] and value not in [square[r][col] for r in range(N)]:
                    square[row][col] = value
                    square[col][row] = N - value + 1
                    break
    
    return "POSSIBLE\n" + "\n".join(" ".join(map(str, row)) for row in square)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        result = generate_latin_square(N, K)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i + 1}: {result}")

if __name__ == "__main__":
    main()