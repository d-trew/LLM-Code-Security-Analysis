import sys
input = sys.stdin.readlines

def min_turns(N, grid):
    x, y = grid[0][0], grid[0][1]
    visited = set()
    moves = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    for i in range(1, N):
        r, c = grid[i][0], grid[i][1]
        visited.add((r,c))

    turns = 0
    while len(visited) < N:
        for _ in range(4):
            new_x, new_y = x + moves[_ % 4][0], y + moves[_ % 4][1]
            if (new_x, new_y) not in visited:
                x, y = new_x, new_y
                turns += 1
                break
        else:
            turns += 1

    return turns

T = int(input()[0].strip())
for _ in range(T):
    N = int(input()[0])
    grid = [list(map(int, input().split())) for _ in range(N)]
    print("Case #{}: {}".format(_ + 1, min_turns(N, grid)))