def main():
    T = int(input())
    for i in range(T):
        N, P = map(int, input().split())
        Xs = []
        for _ in range(N):
            Xs.append(list(map(int, input().split()))
        min_presses = 0
        current_pressure = 0
        for j in range(P):
            pressures = [Xs[k][j] for k in range(len(Xs))]
            target_pressure = max(pressures)
            diff = target_pressure - current_pressure
            if diff > 0:
                min_presses += diff
                current_pressure += diff
        print("Case #%d: %d" % (i+1, min_presses))

main()