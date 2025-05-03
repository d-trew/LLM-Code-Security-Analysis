import math

T = int(input())
for t in range(T):
    N, S = map(int, input().split())
    asteroids = []
    for _ in range(N):
        xi, yi, zi, Vxi, Vyi, Vzi = map(float, input().split())
        asteroid = [xi, yi, zi]
        distance = math.sqrt((Vxi * Vxi) + (Vyi * Vyi) + (Vzi * Vzi))
        asteroids.append([asteroid, distance])
    max_distance = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(asteroids[i][0][0] - asteroids[j][0][0]) <= S:
                max_distance = max(max_distance, math.sqrt(((asteroids[i][0][0] - asteroids[j][0][0]) * (asteroids[i][0][0] - asteroids[j][0][0])) + ((asteroids[i][0][1] - asteroids[j][0][1]) * (asteroids[i][0][1] - asteroids[j][0][1])) + ((asteroids[i][0][2] - asteroids[j][0][2]) * (asteroids[i][0][2] - asteroids[j][0][2]))))
    print("Case #" + str(t+1) + ": " + str(max_distance))