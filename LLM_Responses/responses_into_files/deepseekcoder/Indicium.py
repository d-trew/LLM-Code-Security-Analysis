def generate_latin_square(n, k):
    if n * (n*n + 1) // 2 < k:
        return "IMPOSSIBLE"
    
    matrix = [[0]*n for _ in range(n)]
    numbers = list(range(1, n+1))
    
    for i in range(n):
        row = [numbers[(i+j)%n] for j in range(k)]
        if sum(row) != k:
            return "IMPOSSIBLE"
        matrix[i] = row
        
    return "\n".join(" ".join(str(cell) for cell in row) for row in matrix)

t = int(input().strip())
for i in range(1, t + 1):
    n, k = map(int, input().strip().split())
    result = generate_latin_square(n, k)
    
    if "IMPOSSIBLE" not in result:
        print(f"Case #{i}: POSSIBLE")
        print(result)
    else:
        print(f"Case #{i}: {result}")