def build_diagonal_connections(matrix):
    R = len(matrix)
    C = len(matrix[0])
    
    for i in range(R - 1):
        for j in range(C - 1):
            if matrix[i][j] == 'A' and matrix[i + 1][j + 1] == 'B':
                return 'IMPOSSIBLE'
            elif matrix[i][j] == 'B' and matrix[i + 1][j + 1] == 'A':
                return 'IMPOSSIBLE'
    
    for i in range(R - 1):
        for j in range(C - 1):
            if matrix[i][j] == 'A' and matrix[i + 1][j + 1] == 'A':
                if matrix[i + 1][j] != 'A' or matrix[i][j + 1] != 'A':
                    return 'IMPOSSIBLE'
    
    for i in range(R - 1):
        for j in range(C - 1):
            if matrix[i][j] == 'B' and matrix[i + 1][j + 1] == 'B':
                if matrix[i + 1][j] != 'B' or matrix[i][j + 1] != 'B':
                    return 'IMPOSSIBLE'
    
    for i in range(R - 1):
        for j in range(C - 1):
            if matrix[i][j] == 'A' and matrix[i + 1][j + 1] == '.':
                matrix[i + 1][j + 1] = '/'
            elif matrix[i][j] == 'B' and matrix[i + 1][j + 1] == '.':
                matrix[i + 1][j + 1] = '\\'
    
    return '\n'.join([''.join(row) for row in matrix])

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        R, C = map(int, data[index:index + 2])
        index += 2
        matrix = [list(data[index + i * C:index + (i + 1) * C]) for i in range(R)]
        index += R
        
        result = build_diagonal_connections(matrix)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i + 1}: {result}")

if __name__ == "__main__":
    main()