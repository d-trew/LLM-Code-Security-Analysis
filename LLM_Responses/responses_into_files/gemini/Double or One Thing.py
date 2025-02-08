def solve():
    S = input()
    n = len(S)
    ans = ""
    
    for i in range(1 << n):
        cur = ""
        for j in range(n):
            if (i >> j) & 1:
                cur += S[j] * 2
            else:
                cur += S[j]
        if ans == "" or cur < ans:
            ans = cur
    return ans

T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: {solve()}")