import sys
input = sys.stdin.readlines

def solve(n, p):
    grid = [[0] * n for _ in range(n)]
    x, y = 0, n - 2
    moves = ['E' * (n - 1) + 'S', 'S' * (n - 1) + 'E']

    for i, c in enumerate(p):
        if c == p[i+1] and (x, y + 1 if c == 'E' else y + n if c == 'S'):
            moves.remove(moves[i % 2])
        elif c == 'E':
            grid[x][y] = 1
            x += 1
        elif c == 'S':
            grid[x][y] = 1
            y += n

    path = []
    for i in range(len(moves)):
        if all(grid[(j // n) + (i % 2) * (n - 1)][j % n] == 0 for j in range(len(moves[i]))):
            path += moves[i]
    return 'Case #1: ' + ''.join(path)

for _ in range(int(input()[0].strip())):
    n = int(input()[0].strip())
    p = list(input()[1].strip())
    print(solve(n, p))