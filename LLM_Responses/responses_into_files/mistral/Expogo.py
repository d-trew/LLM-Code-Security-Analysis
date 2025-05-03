from itertools import count, chain, product

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_shortest_path(x, y):
    steps = [(0, 0)]
    directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

    queue = [steps]

    while queue:
        steps = queue.pop(0)
        x, y = steps[-1]

        if (x, y) == (x, y):  # base case: we've reached the goal
            return ''.join(map(lambda d: d[1], steps))

        for direction, step in product(['N', 'S', 'E', 'W'], range(1, manhattan_distance(*steps[-1], x, y) + 2)):
            nx, ny = x + directions[direction][0] * (step - 1), y + directions[direction][1] * (step - 1)
            if manhattan_distance(nx, ny, x, y) <= step:
                queue.append([*steps, (nx, ny)])

    return "IMPOSSIBLE"

def main():
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        print(f'Case #{_ + 1}: {find_shortest_path(0, 0)}')

main()