def main():
    T = int(input())
    for i in range(1, T+1):
        N, L = map(int, input().split())
        C = list(map(int, input().split()))
        max_sum = 0
        total = sum(C)
        for c in C:
            max_sum += (c + 4) // 5 * 5 # rounding up to the nearest multiple of 5
        print("Case #{}: {}".format(i, max_sum))
main()