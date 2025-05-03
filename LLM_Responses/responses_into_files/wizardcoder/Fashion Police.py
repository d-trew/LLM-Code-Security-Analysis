def main():
    T = int(input())
    for i in range(T):
        J, P, S, K = map(int, input().split())
        max_days = min(J * P * S // (K + 1), P * S)
        print("Case #{}: {}".format(i+1, max_days))
        if max_days == 0:
            continue
        for j in range(min(J, K+1)):
            for p in range(min(P, K+1):
                shirt = (j * S) // (K + 1)
                print("{} {} {}".format(j, p, shirt))

if __name__ == "__main__":
    main()