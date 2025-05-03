import math

def pancake_cuts():
    t = int(input())
    for _ in range(t):
        n, d = map(int, input().split())
        angles = list(map(int, input().split()))
        total_cuts = 0
        slices = [angles[0]]
        while len(slices) < d:
            new_slices = []
            for i, angle in enumerate(slices):
                half_angle = angle / 2.0
                if math.isclose(half_angle, int(half_angle)):
                    half_angle = int(half_angle)
                else:
                    half_angle = int(math.floor(half_angle)) + 1
                new_slices.append(half_angle)
                new_slices.append(angle - half_angle)
            slices = new_slices
            total_cuts += len(new_slices) - len(slices)
        print('Case #{}: {}'.format(_, total_cuts))

pancake_cuts()