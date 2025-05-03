t = int(input())
for _ in range(t):
    s = input()
    d = int(input())
    MOD = 10**9 + 7
    n = len(s)
    ans = 0
    for mask in range(2**(n-1)):
        flag = True
        for i in range(n - 1):
            if ((mask >> (i)) & 1) == 0:
                continue
            a, b = int(s[i]), int(s[i+1])
            if (a // d + b // d) % d != 0:
                flag = False
                break
        if flag:
            ans += 1
    print(f"Case #{_+1}: {ans % MOD}")