def solve():
    Hd, Ad, Hk, Ak, B, D = map(int, input().split())

    q = [(Hd, Ad, Hk, Ak, 0)]  # (health, attack, knight_health, knight_attack, turns)
    visited = set()
    visited.add((Hd, Ad, Hk, Ak))

    while q:
        h, a, hk, ak, turns = q.pop(0)

        if hk <= 0:
            return turns + 1

        if h <= 0:
            continue

        # Attack
        next_hk = hk - a
        next_h = h - ak if next_hk > 0 else h
        if (next_h, a, next_hk, ak) not in visited and next_h > 0:
            q.append((next_h, a, next_hk, ak, turns + 1))
            visited.add((next_h, a, next_hk, ak))

        # Buff
        next_a = a + B
        next_hk = hk - a
        next_h = h - ak if next_hk > 0 else h
        if (next_h, next_a, next_hk, ak) not in visited and next_h > 0:
            q.append((next_h, next_a, next_hk, ak, turns + 1))
            visited.add((next_h, next_a, next_hk, ak))

        # Cure
        next_h = Hd
        next_hk = hk - a
        next_h = next_h - ak if next_hk > 0 else next_h
        if (next_h, a, next_hk, ak) not in visited and next_h > 0:
            q.append((next_h, a, next_hk, ak, turns + 1))
            visited.add((next_h, a, next_hk, ak))


        # Debuff
        next_ak = max(0, ak - D)
        next_hk = hk - a
        next_h = h - next_ak if next_hk > 0 else h
        if (next_h, a, next_hk, next_ak) not in visited and next_h > 0:
            q.append((next_h, a, next_hk, next_ak, turns + 1))
            visited.add((next_h, a, next_hk, next_ak))

    return "IMPOSSIBLE"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")