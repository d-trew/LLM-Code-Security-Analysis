T = int(input())
for _ in range(T):
    S = input()
    res = ''
    for c in S:
        if c * 2 in S:
            res += c * 2
        else:
            res += c
    print(f"Case #{_+1}: {res}")