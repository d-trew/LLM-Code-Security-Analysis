def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def intersect(p1, q1, p2, q2):
    return (cross_product(p1, q1, p2) * cross_product(p1, q1, q2) < 0 and
            cross_product(p2, q2, p1) * cross_product(p2, q2, q1) < 0)

def solve():
    N = int(input())
    poles = []
    for _ in range(N):
        x, y = map(int, input().split())
        poles.append((x, y))
    
    existing_fences = []
    for _ in range(2):
        p, q = map(int, input().split())
        existing_fences.append((p - 1, q - 1))

    added_fences = []
    
    for i in range(N):
        for j in range(i + 1, N):
            valid = True
            new_fence = (i, j)
            
            for existing_fence in existing_fences:
                if intersect(poles[new_fence[0]], poles[new_fence[1]], poles[existing_fence[0]], poles[existing_fence[1]]):
                    valid = False
                    break
            
            for added_fence in added_fences:
                if intersect(poles[new_fence[0]], poles[new_fence[1]], poles[added_fence[0]], poles[added_fence[1]]):
                    valid = False
                    break

            if valid:
                added_fences.append(new_fence)

    return len(added_fences), added_fences


T = int(input())
for i in range(1, T + 1):
    num_added_fences, added_fences = solve()
    print(f"Case #{i}: {num_added_fences}")
    for fence in added_fences:
        print(fence[0] + 1, fence[1] + 1)