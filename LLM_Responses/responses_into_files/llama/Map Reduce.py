T = int(input())
for _ in range(T):
    R, C, D = [int(x) for x in input().split()]
    map_data = [list(input()) for _ in range(R)]
    start_pos = None
    finish_pos = None
    for i in range(R):
        for j in range(C):
            if map_data[i][j] == 'S':
                start_pos = (i, j)
            elif map_data[i][j] == 'F':
                finish_pos = (i, j)

    def bfs(map_data, start_pos, finish_pos):
        R, C = len(map_data), len(map_data[0])
        queue = [(start_pos, 0)]
        visited = set([start_pos])
        while queue:
            pos, dist = queue.pop(0)
            if pos == finish_pos:
                return dist
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = pos[0] + x, pos[1] + y
                if 0 <= new_x < R and 0 <= new_y < C and map_data[new_x][new_y] != '#' and (new_x, new_y) not in visited:
                    queue.append(((new_x, new_y), dist + 1))
                    visited.add((new_x, new_y))

    def dfs(map_data, start_pos, finish_pos):
        R, C = len(map_data), len(map_data[0])
        queue = [(start_pos, 0)]
        visited = set([start_pos])
        while queue:
            pos, dist = queue.pop(0)
            if pos == finish_pos:
                return dist
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = pos[0] + x, pos[1] + y
                if 0 <= new_x < R and 0 <= new_y < C and map_data[new_x][new_y] != '#' and (new_x, new_y) not in visited:
                    queue.append(((new_x, new_y), dist + 1))
                    visited.add((new_x, new_y))

    def check(map_data, D):
        R, C = len(map_data), len(map_data[0])
        for i in range(R):
            for j in range(C):
                if map_data[i][j] == '#':
                    temp_map = [list(x) for x in map_data]
                    temp_map[i][j] = '.'
                    if bfs(temp_map, start_pos, finish_pos) == D:
                        return 'POSSIBLE'
        return 'IMPOSSIBLE'

    print(f'Case #{"{}":>1}: {check(map_data, D)}')