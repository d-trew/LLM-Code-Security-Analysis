Here's the Python code for your problem:


def min_jumps(x, y):
    path = []
    while x or y:
        if abs(x) > abs(y):
            if x > 0:
                path.append('E')
                x -= 2**(len(path)-1)
            else:
                path.append('W')
                x += 2**(len(path)-1)
        else:
            if y > 0:
                path.append('N')
                y -= 2**(len(path)-1)
            else:
                path.append('S')
                y += 2**(len(path)-1)
    return ''.join(path[::-1]) if path else 'IMPOSSIBLE'

T = int(input())
for i in range(1, T+1):
    X, Y = map(int, input().split())
    print('Case #{}: {}'.format(i, min_jumps(X, Y)))


This program works by simulating the jumps. It starts at point (0, 0) and makes jumps in a greedy manner towards the goal point. The direction of each jump is chosen to maximize the distance it covers until it reaches the goal or exceeds it. At each step, if moving east or west would cover more distance than moving north or south, it moves that way; otherwise, it moves the other way. This ensures we are always making the largest possible steps towards reaching our goal. The path taken is stored as a list of characters representing the direction of each jump, and then reversed to get the correct order (since we started from the target point). If no jumps were made (i.e., the target was already at (0, 0)), 'IMPOSSIBLE' is returned.