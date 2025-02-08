import math

def solve():
    N = int(input())
    lasers = []
    for _ in range(N):
        x, y, x_prime, y_prime = map(int, input().split())
        lasers.append(((x, y), (x_prime, y_prime)))

    def get_angle(p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        return math.atan2(dy, dx)

    angles = []
    for (x, y), (x_prime, y_prime) in lasers:
        angle = get_angle((x, y), (x_prime, y_prime))
        angles.append(angle)

    def check_coverage(directions):
        min_angle = -float('inf')
        max_angle = float('inf')
        for i in range(N):
            angle = angles[i]
            if directions[i] == 1:  #counterclockwise
                min_angle = max(min_angle, angle)
            else: #clockwise
                max_angle = min(max_angle, angle)

        return max_angle <= min_angle


    total_combinations = 2**N
    uncovered_combinations = 0

    for i in range(total_combinations):
        binary = bin(i)[2:].zfill(N)
        directions = [int(bit) for bit in binary]
        if not check_coverage(directions):
            uncovered_combinations += 1

    return uncovered_combinations / total_combinations


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")