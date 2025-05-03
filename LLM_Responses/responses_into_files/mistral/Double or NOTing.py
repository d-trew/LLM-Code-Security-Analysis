import sys

def transform(s, e):
    t = list(s)
    res = len(e) - len(s)
    for i in range(res):
        t.insert(0, '0')
    while s != e:
        if s == t:
            break
        if s < t:
            t = ''.join('1' if c == '0' else '0' for c in t)
        else:
            t = ''.join('0' if c == '1' else '1' for c in t)
        res += 1
    return res

t = int(input())
for _ in range(t):
    s, e = input().split()
    print(f"Case # {_+1}: {transform(s, e) if s != e else 'IMPOSSIBLE'}")