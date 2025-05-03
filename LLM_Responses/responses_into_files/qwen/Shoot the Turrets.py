def destroy_turrets(R, C, M, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def in_bounds(x, y):
        return 0 <= x < R and 0 <= y < C
    
    def can_destroy(sx, sy, tx, ty):
        for dx, dy in directions:
            nx, ny = sx + dx, sy + dy
            while in_bounds(nx, ny) and grid[nx][ny] != '#':
                if (nx, ny) == (tx, ty):
                    return True
                nx += dx
                ny += dy
        return False
    
    soldiers = [(i, j) for i in range(R) for j in range(C) if grid[i][j] == 'S']
    turrets = [(i, j) for i in range(R) for j in range(C) if grid[i][j] == 'T']
    
    max_destroyed = 0
    result = []
    
    def backtrack(destroyed, moves_left):
        nonlocal max_destroyed, result
        if destroyed > max_destroyed:
            max_destroyed = destroyed
            result = [(s[0], s[1], t[0], t[1]) for s, t in zip(soldiers[:destroyed], turrets[:destroyed])]
        
        if destroyed == len(turrets):
            return
        
        for i in range(len(soldiers)):
            sx, sy = soldiers[i]
            for dx, dy in directions:
                nx, ny = sx + dx, sy + dy
                while in_bounds(nx, ny) and grid[nx][ny] != '#':
                    if (nx, ny) == turrets[destroyed]:
                        soldiers[i] = (nx, ny)
                        backtrack(destroyed + 1, moves_left - 1)
                        break
                    nx += dx
                    ny += dy
    
    backtrack(0, M * len(soldiers))
    
    return max_destroyed, result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        R = int(data[index])
        C = int(data[index + 1])
        M = int(data[index + 2])
        grid = [data[index + 3 + i] for i in range(R)]
        index += 3 + R
        
        destroyed, moves = destroy_turrets(R, C, M, grid)
        
        results.append(f"Case #{_+1}: {destroyed}")
        if moves:
            for s_i, t_i in moves:
                results.append(f"{s_i} {t_i}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()