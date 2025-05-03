T = int(input())
for t in range(1, T+1):
    x, y, m = [int(i) for i in input().split()] + list(input().strip())
    px, py = 0, 0
    for move in m:
        if move == 'N':
            py += 1
        elif move == 'S':
            py -= 1
        elif move == 'E':
            px += 1
        elif move == 'W':
            px -= 1
    dx = abs(x - px)
    dy = abs(y - py)
    if min(dx, dy) <= 5:
        print(f"Case #{t}: {min(dx, dy)}")
    else:
        print("Case #{}: IMPOSSIBLE".format(t))