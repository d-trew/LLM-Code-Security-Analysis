def is_square_free(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i + 1 < len(matrix) and j + 1 < len(matrix[0]) and 
                matrix[i][j] == '/' and matrix[i+1][j+1] == '/' and 
                matrix[i][j+1] == '\\' and matrix[i+1][j] == '\\'):
                return False
    return True

def solve(R, C, S, D):
    if sum(S) != sum(D):
        return "IMPOSSIBLE"
    
    from itertools import product
    
    for diagonals in product(['/', '\\'], repeat=R*C):
        matrix = [list(diagonals[i*C:(i+1)*C]) for i in range(R)]
        if is_square_free(matrix) and sum(row.count('/') for row in matrix) == sum(S) and sum(col.count('/') for col in zip(*matrix)) == sum(D):
            return "POSSIBLE\n" + '\n'.join(''.join(row) for row in matrix)
    
    return "IMPOSSIBLE"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        R, C = map(int, data[index:index+2])
        S = list(map(int, data[index+2:index+2+R]))
        D = list(map(int, data[index+2+R:index+2+R+C]))
        index += 2 + R + C
        
        result = solve(R, C, S, D)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    main()