import sys
input = sys.stdin.readlines

def solve(n, c, m, positions, buyers):
    pos_map = {p: i for i, p in enumerate(sorted(positions))}
    rides, promotions = 0, 0
    used_buyers = set()
    seats = [0] * n

    def assign(b):
        for seat in reversed(range(n)):
            if not seats[seat]:
                seats[seat] = b
                used_buyers.add(b)
                break

    for p, b in sorted((pos_map[p], b) for p, b in zip(positions, buyers)):
        if not used_buyers or b != min(used_buyers):
            assign(b)
            promotions += 1
            rides += 1
        elif p > 1:
            seats[p - 1] = b
            promotions += 1
            rides -= 1
        else:
            rides += 1

    return rides, promotions

T = int(input()[0])
for _ in range(T):
    n, c, m = map(int, input().split())
    positions, buyers = list(map(list, zip(*[(map(int, line.split()) for line in input()]))))
    rides, promotions = solve(n, c, m, positions, buyers)
    print("Case #{}: {} {}".format(_ + 1, rides, promotions))