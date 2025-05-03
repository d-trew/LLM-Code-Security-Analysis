def solve():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        bffs = list(map(int, input().split()))
        seen = set()
        circle_size = 0
        for j in range(n):
            if bffs[j] not in seen:
                seen.add(bffs[j])
                circle_size += 2
            else:
                seen.remove(seen.pop())
                circle_size += 1
        print(f"Case #{i}: {circle_size}")

solve()