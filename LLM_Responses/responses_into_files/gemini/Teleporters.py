def l1_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

def solve():
    N = int(input())
    planets = []
    for _ in range(N + 2):
        x, y, z = map(int, input().split())
        planets.append((x, y, z))

    thundera = planets[0]
    care_a_lot = planets[1]
    teleporters = planets[2:]

    q = [(thundera, 0)]
    visited = {thundera}

    while q:
        curr_pos, dist = q.pop(0)
        if curr_pos == care_a_lot:
            return dist

        for i, teleporter in enumerate(teleporters):
            dist_to_teleporter = l1_distance(curr_pos, teleporter)
            for j, teleporter2 in enumerate(teleporters):
                
                new_x = teleporter[0] + (curr_pos[0] - teleporter[0])
                new_y = teleporter[1] + (curr_pos[1] - teleporter[1])
                new_z = teleporter[2] + (curr_pos[2] - teleporter[2])

                
                new_pos = (new_x, new_y, new_z)
                
                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append((new_pos, dist + 1))

    return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")