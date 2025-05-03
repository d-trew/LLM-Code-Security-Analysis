import math
def checker(N):
    pairs = []
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        pairs.append([[x1, y1], [x2, y2]])
    # find intersections between paths
    intersections = []
    for i in range(N):
        for j in range(i + 1, N):
            x_int, y_int = math.gcd(pairs[i][0][0] - pairs[j][0][0], pairs[i][1][0] - pairs[j][1][0]), \
                           math.gcd(pairs[i][0][1] - pairs[j][0][1], pairs[i][1][1] - pairs[j][1][1])
            if x_int > 0 and y_int > 0:
                intersections.append([i, j])
    # check if there are at most 25 pairs that fail to intersect every other pair
    if len(intersections) <= 25:
        return "MAGNIFICENT"
    else:
        return [str(pair[0] + 1) for pair in intersections]