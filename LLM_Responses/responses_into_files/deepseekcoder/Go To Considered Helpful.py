T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    son_location = None
    for i in range(R):
        row = input()
        if 'N' in row:
            son_location = (i, row.index('N'))
        if 'M' in row:
            Marlin_location = (i, row.index('M'))
    if not son_location:
        print("Case #{}: IMPOSSIBLE".format(_ + 1))
        continue
    directions = []
    while True:
        x, y = Marlin_location
        dx, dy = 0, 0
        if 'N' in row[x+1]: 
            dx += 1
        elif 'S' in row[x-1]:
            dx -= 1
        if 'E' in row[y+1]:
            dy += 1
        elif 'W' in row[y-1]:
            dy -= 1
        directions.append('N' if dx > 0 else 'S' if dx < 0 else '')
        directions.append('E' if dy > 0 else 'W' if dy < 0 else '')
        Marlin_location = (x + dx, y + dy)
        if Marlin_location == son_location:
            break
    print("Case #{}: {}".format(_ + 1, len(directions)))