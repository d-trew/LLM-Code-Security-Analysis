import math
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def get_ratio(x1, y1, x2, y2):
    d = math.gcd(math.gcd(x1, y1), math.gcd(x2, y2))
    return f"{x1 // d}/{y1 // d}", f"{x2 // d}/{y2 // d}"

def get_intersecting_segments(polygon):
    intersecting_pairs = set()
    for i in range(len(polygon)):
        p1, p2 = polygon[i], polygon[(i + 1) % len(polygon)]
        for j in range(i + 2, len(polygon)):
            q1, q2 = polygon[j], polygon[(j + 1) % len(polygon)]
            if (p1, p2) == (q1, q2):
                continue
            x1, y1, x2, y2 = p1[0] - p2[0], p1[1] - p2[1], q1[0] - q2[0], q1[1] - q2[1]
            if x1 * (y2 - p2[1]) == y1 * (x2 - p2[0]) and (p1, q1) != (p2, q2):
                intersecting_pairs.add(frozenset([polygon[i], polygon[(i + 1) % len(polygon)]))
    return intersecting_pairs

def find_neat_folding_patterns(polygon, k):
    if k == 2:
        return get_intersecting_segments(polygon)
    
    def is_neat(segment1, segment2, segments):
        for segment in segments:
            if segment != segment1 and segment[0] not in segment1 and segment[1] not in segment1:
                return False
            if segment != segment2 and segment[0] not in segment2 and segment[1] not in segment2:
                return False
        return True
    
    def get_neat_segments(polygon, k):
        segments = []
        for i in range(len(polygon)):
            p1, p2 = polygon[i], polygon[(i + 1) % len(polygon)]
            for j in range(i + 2, len(polygon)):
                q1, q2 = polygon[j], polygon[(j + 1) % len(polygon)]
                if (p1, p2) == (q1, q2):
                    continue
                x1, y1, x2, y2 = p1[0] - p2[0], p1[1] - p2[1], q1[0] - q2[0], q1[1] - q2[1]
                if x1 * (y2 - p2[1]) == y1 * (x2 - p2[0]):
                    segment = frozenset([p1, p2])
                    segments.append(segment)
        for _ in range(k - 3):
            new_segments = []
            for i, s1 in enumerate(segments):
                for j, s2 in enumerate(segments[i + 1:], start=i + 1):
                    if is_neat(s1, s2, segments) and not (is_neat(s2, s1, segments)):
                        new_segment = tuple(sorted([*s1, *s2]))
                        if not any(new_segment[0] in segment for segment in segments):
                            new_segments.append(new_segment)
            segments += new_segments
        return set(map(tuple, segments[-k:])
    
    neat_patterns = get_neat_segments(polygon, k + 1)
    if len(neat_patterns) >= k:
        return list(neat_patterns)[-k:]
    else:
        return None

def main():
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        polygon = []
        for _ in range(N):
            x, y = map(int, input().split())
            polygon.append((x, y))
        
        neat_patterns = find_neat_folding_patterns(polygon, K - 1)
        if neat_patterns:
            print("Case #%d: POSSIBLE" % (i + 1))
            for segment in neat_patterns:
                x1, y1 = min(segment[0][0], segment[1][0]), min(segment[0][1], segment[1][1])
                x2, y2 = max(segment[0][0], segment[1][0]), max(segment[0][1], segment[1][1])
                print("A%sB%s" % (get_ratio(x1, y1, x2, y2)) if x1 == x2 else "A%s/%dB%s/%d" % (x1 // lcm(x1, y1), y1 // gcd(x1, y1), x2 // lcm(x1, y1), y2 // gcd(x1, y1)))
        else:
            print("Case #%d: IMPOSSIBLE" % (i + 1))
        
if __name__ == "__main__":
    main()