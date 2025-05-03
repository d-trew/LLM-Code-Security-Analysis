import sys
import math
input = sys.stdin.readlines

def solve(data):
    D, N = map(int, data[0].split())
    horses = [list(map(int, line.split())) for line in data[1:]]
    speeds = [float('inf')] + [horses[i][1] for i in range(N)]
    distances = []
    for horse in horses:
        distances.append(D - horse[0])
    distances.sort()

    max_speed = 0
    for distance in distances:
        for speed in speeds:
            if distance > speed:
                break
        max_speed = min(max_speed, speed)

    return f"Case #1: {max_speed}"

if __name__ == "__main__":
    T = int(input()[0])
    for _ in range(T):
        print(solve(list(map(str.strip, input()))))