def solve():
    x, y = map(int, input().split())

    q = [("", 0, 0)]
    visited = set()
    visited.add((0,0))

    while q:
        path, cur_x, cur_y = q.pop(0)

        if cur_x == x and cur_y == y:
            return path

        next_move = 1
        for move in ["N", "S", "E", "W"]:
            next_x, next_y = cur_x, cur_y
            if move == "N":
                next_y += next_move
            elif move == "S":
                next_y -= next_move
            elif move == "E":
                next_x += next_move
            elif move == "W":
                next_x -= next_move

            if (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                q.append((path + move, next_x, next_y))

        next_move *= 2


    return "IMPOSSIBLE"

t = int(input())
for i in range(1, t + 1):
    result = solve()
    print(f"Case #{i}: {result}")