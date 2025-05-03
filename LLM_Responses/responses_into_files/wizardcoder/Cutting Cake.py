import fractions

def get_enjoyment(x, y, a, b):
    return abs((x * (a + b) / 2) - x * a) if x <= 0 else abs((W - x) * (b - a) / 2)

T = int(input())
for i in range(1, T + 1):
    N, W, H = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    XYAB = [tuple(map(float, input().split())) for _ in range(N)]
    
    left_enjoyment = 0.0
    right_enjoyment = 0.0
    min_diff = float('inf')
    for x in range(-1, W - max(P, R) + 2):
        patches = []
        for X, Y, A, B in XYAB:
            if (X + P) * Q / 2 <= y < (X + R) * S / 2:
                left_enjoyment += get_enjoyment(x - X, Y, A, B)
            elif x >= (X + P) and x <= W - max(P, R):
                right_enjoyment += get_enjoyment(x - (W - X), H - Y - Q, A, B)
        diff = abs(left_enjoyment - right_enjoyment)
        if diff < min_diff:
            min_diff = diff
    
    print("Case #{}: {}/{}".format(i, fractions.Fraction(min_diff).limit_denominator()))