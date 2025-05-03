def main():
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        Ci = list(map(int, input().split()))
        Di = list(map(int, input().split())
        count = 0
        for L in range(1, N+1):
            for R in range(L, N+1):
                if max(Ci[L-1:R]) - min(Di) <= K and max(Di[L-1:R]) - min(Ci) <= K:
                    count += 1
        print("Case #%d: %d" % (i+1, count))
main()