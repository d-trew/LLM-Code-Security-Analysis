def solve():
    P, Q = map(int, input().split())
    people = []
    for _ in range(P):
        x, y, d = input().split()
        people.append((int(x), int(y), d))

    best_count = -1
    best_x = -1
    best_y = -1

    for x in range(Q + 1):
        for y in range(Q + 1):
            count = 0
            for px, py, d in people:
                if d == 'N' and y > py:
                    count += 1
                elif d == 'S' and y < py:
                    count += 1
                elif d == 'E' and x > px:
                    count += 1
                elif d == 'W' and x < px:
                    count += 1

            if count > best_count:
                best_count = count
                best_x = x
                best_y = y
            elif count == best_count:
                if x < best_x:
                    best_x = x
                    best_y = y
                elif x == best_x and y < best_y:
                    best_y = y

    return f"{best_x} {best_y}"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")