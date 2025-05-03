def main():
    T = int(input())
    for i in range(1, T+1):
        N, K = map(int, input().split())
        max_LS = min_RS = 0
        if K == 1 and (N % 2) != 0:
            print("Case #{}: {} {}".format(i, N//2, 0)
        else:
            for j in range(K-1):
                max_LS = N - j - 1 if j < N//2 else j + 1
                min_RS = j if j < N//2 else N - j - 1
            print("Case #{}: {} {}".format(i, max_LS, min_RS))<|im_sep|>