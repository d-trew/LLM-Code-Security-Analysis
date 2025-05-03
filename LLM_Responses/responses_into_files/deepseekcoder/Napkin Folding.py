from fractions import Fraction
import sys

def is_neat(napkin, k):
    for i in range(k-1):
        x0 = napkin[i][0]
        y0 = napkin[i][1]
        x1 = napkin[(i+1)%k][0]
        y1 = napkin[(i+1)%k][1]
        if is_collinear(x0, y0, x1, y1):
            return False
    return True

def is_collinear(x0, y0, x1, y1):
    dx = (x1 - x0)
    dy = (y1 - y0)
    dxdy = (dx * dy) if dx != 0 else float('inf')
    d2 = max((abs(dx)), (abs(dy)))
    return abs(dxdy) <= d2

def find_pattern(napkin, k):
    for i in range(len(napkin)-1):
        x0 = napkin[i][0]
        y0 = napkin[i][1]
        x1 = napkin[(i+1)%len(napkin)][0]
        y1 = napkin[(i+1)%len(napkin)][1]
        if is_collinear(x0, y0, x1, y1):
            for j in range(len(napkin)-1):
                x2 = napkin[j][0]
                y2 = napkin[j][1]
                x3 = napkin[(j+1)%len(napkin)][0]
                y3 = napkin[(j+1)%len(napkin)][1]
                if is_collinear(x2, y2, x3, y3):
                    continue
                for _ in range(k-1):
                    return [(Fraction(x0), Fraction(y0)), (Fraction(x1), Fraction(y1))]
    return None

def main():
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())
        napkin = []
        for _ in range(N):
            x, y = map(int, input().split())
            napkin.append((x, y))
        if is_neat(napkin, K):
            print(f"Case #{t+1}: POSSIBLE")
            pattern = find_pattern(napkin, K)
            if pattern:
                for segment in pattern:
                    print(*segment)
        else:
            print(f"Case #{t+1}: IMPOSSIBLE")

if __name__ == "__main__":
    main()