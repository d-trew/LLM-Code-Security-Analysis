def is_tidy(n):
    str_n = str(n)
    for i in range(len(str_n)-1):
        if int(str_n[i]) > int(str_n[i+1]):
            return False
    return True

def next_tidy(n):
    str_n = list(str(n))
    for i in range(len(str_n)-1, 0, -1):
        if int(str_n[i]) < int(str_n[i-1]):
            str_n[i] = '9'
            str_n[i-1] = str(int(str_n[i-1])-1)
    if str_n[0] == '0':
        return int(''.join(str_n)[1:])
    else:
        return int(''.join(str_n))

T = int(input())
for t in range(1, T+1):
    N = int(input())
    while not is_tidy(N):
        N = next_tidy(N) - 1
    print("Case #{}: {}".format(t, N))