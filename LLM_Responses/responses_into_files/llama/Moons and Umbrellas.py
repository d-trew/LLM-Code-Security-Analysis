t = int(input())
for _ in range(t):
    x, y, s = [int(i) if i.isdigit() else i for i in input().split()]
    res = float('inf')
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            cnt_cj = s[:i].count('CJ') + s[i:j].count('CJ')
            cnt_jc = s[:i].count('JC') + s[i:j].count('JC')
            res = min(res, x*cnt_cj + y*cnt_jc)
    print(f"Case # {_+1}: {res}")