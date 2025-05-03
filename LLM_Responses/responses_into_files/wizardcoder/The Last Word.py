n = int(input()) # read the number of test cases
for i in range(1, n+1):
    s = input().strip()
    if len(s) % 2 == 0:
        s = 'A' + s[::-1] + 'A'
    else:
        s = 'A' + s[::-1] + 'B'
    print("Case #{}: {}".format(i, sorted([s[:len(s)//2], s[len(s)//2+1:])[0][::-1]) if len(s) > 1 else s)