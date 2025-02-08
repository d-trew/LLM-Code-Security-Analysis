def solve():
    S = input()
    res = ""
    depth = 0
    for digit in S:
        d = int(digit)
        if d > depth:
            res += "(" * (d - depth)
        elif d < depth:
            res += ")" * (depth - d)
        res += digit
        depth = d
    res += ")" * depth
    return res

T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: {solve()}")