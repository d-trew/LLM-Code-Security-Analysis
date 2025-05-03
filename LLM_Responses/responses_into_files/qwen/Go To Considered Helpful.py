import sys

def find_min_program(R, C, matrix):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for dr, dc in directions:
        r, c = R // 2, C // 2
        while True:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= R or nc < 0 or nc >= C or matrix[nr][nc] == '#':
                break
            if matrix[nr][nc] == 'N':
                return 1
            r, c = nr, nc
    return "IMPOSSIBLE"

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    for _ in range(T):
        R = int(data[index])
        C = int(data[index + 1])
        matrix = [data[index + 2 + i] for i in range(R)]
        index += 2 + R
        
        result = find_min_program(R, C, matrix)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    main()