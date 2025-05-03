def max_kits(N, P, packages):
    from collections import defaultdict

    def can_form_kit(serving_size, packages):
        needs = [serving_size * r for r in R]
        for i in range(P):
            if not (0.9 * needs[i] <= packages[i][1] <= 1.1 * needs[i]):
                return False
        return True

    packages.sort(key=lambda x: x[1])
    R = [int(input()) for _ in range(N)]
    packages = [[int(input()), int(input())] for _ in range(P)]

    left, right = min(p[0] for p in packages), max(p[0] for p in packages)
    while left < right:
        mid = (left + right + 1) // 2
        if can_form_kit(mid, packages):
            left = mid
        else:
            right = mid - 1

    return left

T = int(input())
for t in range(1, T + 1):
    N, P = map(int, input().split())
    print(f"Case #{t}: {max_kits(N, P, packages)}")