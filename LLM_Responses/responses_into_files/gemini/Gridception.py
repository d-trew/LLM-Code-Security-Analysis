def solve():
    R, C = map(int, input().split())
    grid = [input() for _ in range(R)]

    max_size = 0
    for r in range(R):
        for c in range(C):
            for size in range(1, R * C + 1):
                for dr in range(R + 1 - size):
                    for dc in range(C + 1 - size):
                        pattern = []
                        for i in range(size):
                            row = ""
                            for j in range(size):
                                row += grid[r + i][c + j]
                            pattern.append(row)
                        
                        is_connected = False
                        if size > 0:
                            is_connected = True
                            visited = [[False for _ in range(size)] for _ in range(size)]
                            q = [(0,0)]
                            visited[0][0] = True
                            count = 0
                            while q:
                                cur_r, cur_c = q.pop(0)
                                count += 1
                                for dr2, dc2 in [(0,1),(0,-1),(1,0),(-1,0)]:
                                    nr, nc = cur_r + dr2, cur_c + dc2
                                    if 0 <= nr < size and 0 <= nc < size and not visited[nr][nc]:
                                        visited[nr][nc] = True
                                        q.append((nr,nc))
                            if count != size:
                                is_connected = False

                        if is_connected:
                            max_size = max(max_size, size)

    return max_size


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")