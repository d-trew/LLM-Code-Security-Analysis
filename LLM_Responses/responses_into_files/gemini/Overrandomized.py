def solve():
    U = int(input())
    records = []
    for _ in range(10000):
        line = input().split()
        records.append((int(line[0]) if line[0] != '-1' else -1, line[1]))

    import itertools
    import string

    for perm in itertools.permutations(string.ascii_uppercase):
        d = "".join(perm[:10])
        mapping = {c: i for i, c in enumerate(d)}
        
        possible = True
        for q, r in records:
            if q != -1:
                try:
                    num = 0
                    for c in r:
                        num = num * 10 + mapping[c]
                    if num > q or num < 1:
                        possible = False
                        break
                except KeyError:
                    possible = False
                    break

        if possible:
            return d
    return "No solution found"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")