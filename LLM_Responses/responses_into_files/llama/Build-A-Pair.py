T = int(input())
for _ in range(T):
    D = list(map(int, input()))
    D.sort()
    res = float('inf')
    for i in range(len(D)):
        for j in range(i+1, len(D)):
            a, b = 0, 0
            k, l = 0, i
            while k < l:
                if D[k] > 0:
                    a = a * 10 + D[k]
                    k += 1
                else:
                    k += 1
            while l < len(D):
                if D[l] > 0:
                    b = b * 10 + D[l]
                    l += 1
                else:
                    l += 1
            res = min(res, abs(a - b))
    print("Case #{}: {}".format(_, res))