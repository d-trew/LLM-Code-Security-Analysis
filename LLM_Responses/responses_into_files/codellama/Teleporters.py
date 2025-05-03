import math

def teleport(x1, y1, z1, x2, y2, z2):
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    Thundera_x, Thundera_y, Thundera_z = map(int, input().split())
    CareA Lot_x, CareA Lot_y, CareA Lot_z = map(int, input().split())
    teleporters = []
    for i in range(N):
        x, y, z = map(int, input().split())
        teleporters.append((x, y, z))
    min_teleportations = math.inf
    for i in range(len(teleporters)):
        for j in range(i+1, len(teleporters)):
            distance = teleport(Thundera_x, Thundera_y, Thundera_z, *teleporters[i]) + teleport(*teleporters[i], *teleporters[j]) + teleport(*teleporters[j], CareA Lot_x, CareA Lot_y, CareA Lot_z)
            if distance < min_teleportations:
                min_teleportations = distance
    print("Case #" + str(t) + ": " + str(min_teleportations))