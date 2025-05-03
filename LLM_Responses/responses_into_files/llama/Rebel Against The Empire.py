import math
T = int(input())
for _ in range(T):
    N, S = map(int, input().split())
    asteroids = []
    for _ in range(N):
        x, y, z, Vx, Vy, Vz = map(float, input().split())
        asteroids.append((x, y, z, Vx, Vy, Vz))
    max_distance = 0
    current_position = (0, 0, 0)
    previous_positions = [(0, 0, 0)]
    for i in range(N):
        x, y, z, Vx, Vy, Vz = asteroids[i]
        time_to_meet = ((x - current_position[0]) / Vx + 
                        (y - current_position[1]) / Vy + 
                        (z - current_position[2]) / Vz)
        if time_to_meet > S:
            jump_distance = math.sqrt((x - current_position[0])**2 + 
                                       (y - current_position[1])**2 + 
                                       (z - current_position[2])**2)
            max_distance = max(max_distance, jump_distance)
            previous_positions.append((x, y, z))
        current_position = (x, y, z)
    print('Case #{}: {:.4f'.format(_, max_distance))