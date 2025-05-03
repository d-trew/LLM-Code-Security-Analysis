import sys

def solve(n_test_cases):
    for i in range(1, n_test_cases + 1):
        n = int(input())
        points = []
        max_size = 0
        for j in range(1, n + 1):
            x, y = map(int, input().split())
            points.append((x, y))
        for k in range(1, n + 1):
            for l in range(k + 1, n + 1):
                for m in range(l + 1, n + 1):
                    if is_triangle(points[k - 1], points[l - 1], points[m - 1]):
                        max_size += 1
        print("Case #" + str(i) + ": " + str(max_size))

def is_triangle(p1, p2, p3):
    return (p1[0] != p2[0] and p2[0] != p3[0] and p3[0] != p1[0]) and \
           (p1[1] != p2[1] and p2[1] != p3[1] and p3[1] != p1[1])

if __name__ == "__main__":
    t = int(input())
    solve(t)