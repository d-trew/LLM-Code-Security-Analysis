n = int(input())
for i in range(n):
    t = int(input())
    p = int(input())
    g = list(map(int, input().split()))
    left = 0
    res = 0
    for people in g:
        if people + left > p:
            res += (people+p-1)//p
            left = p - (people+p-1)%p
        else:
            res += 1
            left -= people
    print("Case #{}: {}".format(i+1, res))