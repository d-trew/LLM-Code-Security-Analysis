def cross_product(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    cp1 = cross_product(x2 - x1, y2 - y1, x3 - x1, y3 - y1)
    cp2 = cross_product(x2 - x1, y2 - y1, x4 - x1, y4 - y1)
    cp3 = cross_product(x4 - x3, y4 - y3, x1 - x3, y1 - y3)
    cp4 = cross_product(x4 - x3, y4 - y3, x2 - x3, y2 - y3)
    return (cp1 > 0 and cp2 < 0 or cp1 < 0 and cp2 > 0) and \
           (cp3 > 0 and cp4 < 0 or cp3 < 0 and cp4 > 0)

def solve():
    N = int(input())
    pairs = []
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        pairs.append((x1, y1, x2, y2))

    result = []
    for i in range(N):
        count = 0
        for j in range(N):
            if i != j:
                if intersect(pairs[i][0], pairs[i][1], pairs[i][2], pairs[i][3],
                             pairs[j][0], pairs[j][1], pairs[j][2], pairs[j][3]):
                    count += 1
        if count != N - 1:
            result.append(i + 1)

    if not result:
        return "MAGNIFICENT"
    else:
        return ", ".join(map(str, result))

T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: {solve()}")