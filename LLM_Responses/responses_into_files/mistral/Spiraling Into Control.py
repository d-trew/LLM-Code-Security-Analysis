from collections import deque
import sys
input = sys.stdin.readlines

def spiral_order(n):
    grid = [[0] * n for _ in range(n)]
    count = 1
    i, j = 0, 0
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    di = 0

    while count < n * n:
        grid[i][j] = count
        count += 1
        next_i, next_j = i + dirs[di][0], j + dirs[di][1]
        if (next_i < 0 or next_i >= n or next_j < 0 or next_j >= n or grid[next_i][next_j] != 0):
            di = (di + 1) % 4
            i, j = i + dirs[(di + 3) % 4][0], j + dirs[(di + 3) % 4][1]
    return grid

def find_path(grid, start, end, k):
    visited = set()
    queue = deque([(start, [])])
    while queue:
        room, path = queue.popleft()
        if room == end:
            return path + [end]
        visited.add(room)
        for next_room in get_next_rooms(grid, room):
            if next_room not in visited and (next_room - room - 1) not in visited and next_room <= end:
                queue.append((next_room, path + [room]))
    return None

def get_next_rooms(grid, room):
    i, j = divmod(room - 1, len(grid[0]))
    return [grid[(i + d)[len(grid[0])] % len(grid[0])][(j + d) % len(grid[0]) + 1] for d in range(1, 3)]

def main():
    T = int(input()[0].strip())
    for _ in range(T):
        n, k = map(int, input()[0].split())
        grid = spiral_order(n)
        start, end = (1, 1), (n * n, )
        path = find_path(grid, start, end, k)
        if not path:
            print("Case #{}: IMPOSSIBLE".format(_ + 1))
        else:
            shortcuts = len([x for x in path[1:-1] if x - path[0][-1] > 1])
            print("Case #{}: {}".format(_ + 1, shortcuts))
            for i in range(shortcuts):
                print(*path[i * 2 : (i + 1) * 2 + 2])

if __name__ == "__main__":
    main()