def check_magnificent(T):
    for _ in range(T):
        N = int(input())
        pairs = []
        magnificent = True
        for _ in range(N):
            x1, y1, x2, y2 = map(int, input().split())
            pairs.append(((x1, y1), (x2, y2)))
        for i in range(N):
            for j in range(i+1, N):
                if not intersect(pairs[i][0], pairs[j][0]):
                    magnificent = False
                    break
        if magnificent:
            print(f"Case # {_+1}: MAGNIFICENT")
        else:
            print(f"Case # {_+1}: {' '.join(map(str, range(1, N+1)))}")

def intersect(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        return False
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    for point in [(x1, y1), (x2, y2)]:
        x, y = point
        if a * x + b != y:
            return False
    return True

T = int(input())
check_magnificent(T)