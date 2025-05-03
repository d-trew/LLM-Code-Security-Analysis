T = int(input())
for i in range(1, T+1):
    N, K = map(int, input().split())
    stalls = ['O'] * (N + 2)
    for j in range(K-1):
        if 'O' == stalls[j+1]:
            stalls[j] = 'O'
        else:
            stalls[j+1] = 'O'
    max_ls_rs = 0
    min_ls_rs = float('inf')
    for j in range(2, N + 1):
        ls = 0 if 'O' == stalls[j-1] else j - 1
        rs = 0 if 'O' == stalls[j+1] else N - j
        if min(ls, rs) > min_ls_rs:
            max_ls_rs = max(max_ls_rs, max(ls, rs))
            min_ls_rs = min(ls, rs)
        elif min(ls, rs) == min_ls_rs and max(ls, rs) > max_ls_rs:
            max_ls_rs = max(ls, rs)
    print(f"Case #{i}: {max_ls_rs} {min_ls_rs}")