T = int(input())
for _ in range(T):
    C = int(input())
    B = list(map(int, input().split()))
    rows = [0]
    for b in B:
        if rows[-1] < 2 and (rows[-1] == 1 or sum([int(x != '.') for x in rows[-1]]) > 0):
            rows.append('/\\' * (b + 1))
        else:
            rows.append('.' * (C - 1) + '/' * b)
    print(f"Case #{_+1}: {'IMPOSSIBLE' if len(rows) < C else len(rows)}")
    for row in rows:
        print(row)