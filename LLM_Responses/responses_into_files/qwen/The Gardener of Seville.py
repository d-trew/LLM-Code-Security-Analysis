def can_build_maze(R, C, lovers):
    if R * C == 1:
        return '/' if lovers[0] % 2 != lovers[1] % 2 else 'IMPOSSIBLE'
    
    courtiers = list(range(1, 2 * (R + C) + 1))
    maze = [['.' for _ in range(C)] for _ in range(R)]
    
    def place_hedge(x, y, direction):
        if x < 0 or x >= R or y < 0 or y >= C:
            return False
        if maze[x][y] != '.':
            return False
        maze[x][y] = direction
        return True
    
    for i in range(0, len(lovers), 2):
        a, b = lovers[i] - 1, lovers[i + 1] - 1
        found_path = False
        for dx, dy in [(-1, 1), (1, -1)]:
            if place_hedge(a // C, a % C, '\\') and place_hedge(b // C, b % C, '/'):
                found_path = True
                break
            maze[a // C][a % C], maze[b // C][b % C] = '.', '.'
        if not found_path:
            return 'IMPOSSIBLE'
    
    return '\n'.join(''.join(row) for row in maze)

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
        lovers = list(map(int, data[index:index + 2 * (R + C)]))
        index += 2 * (R + C)
        
        result = can_build_maze(R, C, lovers)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f'Case #{i + 1}: {result}')

if __name__ == "__main__":
    main()