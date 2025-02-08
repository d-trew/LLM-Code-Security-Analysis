import heapq

def solve():
    R, C, D = map(int, input().split())
    grid = [list(input()) for _ in range(R)]

    start_row, start_col = -1, -1
    end_row, end_col = -1, -1
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                start_row, start_col = r, c
            elif grid[r][c] == 'F':
                end_row, end_col = r, c

    def dijkstra(graph):
        distances = { (r,c): float('inf') for r in range(R) for c in range(C)}
        distances[(start_row, start_col)] = 0
        priority_queue = [(0, start_row, start_col)]

        while priority_queue:
            dist, row, col = heapq.heappop(priority_queue)
            if dist > distances[(row, col)]:
                continue
            if (row, col) == (end_row, end_col):
                return dist

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < R and 0 <= new_col < C and graph[new_row][new_col] == '.' and distances[(new_row, new_col)] > dist + 1:
                    distances[(new_row, new_col)] = dist + 1
                    heapq.heappush(priority_queue,(distances[(new_row, new_col)], new_row, new_col))
        return float('inf')

    
    q = [(grid, 0)]
    visited = set()
    while q:
        curr_grid, removed_walls = q.pop(0)
        grid_tuple = tuple(tuple(row) for row in curr_grid)
        if grid_tuple in visited:
            continue
        visited.add(grid_tuple)
        
        dist = dijkstra(curr_grid)
        if dist == D:
            print("POSSIBLE")
            for row in curr_grid:
                print("".join(row))
            return

        for r in range(R):
            for c in range(C):
                if curr_grid[r][c] == '#':
                    new_grid = [row[:] for row in curr_grid]
                    new_grid[r][c] = '.'
                    q.append((new_grid,removed_walls + 1))

    print("IMPOSSIBLE")


T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: ", end="")
    solve()