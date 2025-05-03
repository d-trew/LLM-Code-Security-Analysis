import fractions
from collections import defaultdict

def calculate_probability(lasers):
    points = defaultdict(list)
    for x, y, x', y' in lasers:
        points[x, y].append((x', y'))

    segment_length = 1000
    interval_count = 0
    for point in points:
        start, end = sorted(point)
        if start[1] < 0 or end[1] > segment_length:
            continue
        for i, (p1, p2) in enumerate(zip(points[(start[0], start[1])], points[end])):
            if not p2:
                continue
            overlap = max(min(p1[0][1] - end[1], p2[0][1] - start[1]), 0)
            if overlap > 0:
                interval_count += overlap / segment_length
    return fractions.Fraction(interval_count, len(lasers))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lasers = []
        for _ in range(n):
            x, y, x', y' = map(int, input().split())
            lasers.append((x, y, x', y'))
        print(f"Case #{_ + 1}: {calculate_probability(lasers).limit_denominator()}")

main()