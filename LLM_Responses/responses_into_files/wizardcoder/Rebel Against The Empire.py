def main():
    T = int(input())
    for i in range(T):
        N, S = map(int, input().split())
        asteroids = []
        max_dist = 0
        for _ in range(N):
            x, y, z, Vx, Vy, Vz = map(float, input().split())
            asteroids.append((x, y, z, Vx, Vy, Vz))
        # Your code here to calculate max_dist based on the given constraints and conditions