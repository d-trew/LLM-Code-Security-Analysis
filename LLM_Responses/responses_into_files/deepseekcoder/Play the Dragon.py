def dragon_knight():
    T = int(input())
    for t in range(1, T + 1):
        Hd, Ad, Hk, Ak, B, D = map(int, input().split())
        turns = 0
        while True:
            if Hk <= 0:
                print("Case #{}: {}".format(t, turns))
                break
            else:
                Hd -= max(Ak - B, 0)
                turns += 1
            if Hd <= 0:
                print("Case #{}: IMPOSSIBLE".format(t))
                break
            else:
                Hk -= Ad
                turns += 1
        if Hk > 0 and Hd > 0:
            while True:
                if Hd <= 0:
                    print("Case #{}: {}".format(t, turns))
                    break
                else:
                    Hk -= max(Ad - D, 0)
                    turns += 1
                if Hk <= 0:
                    print("Case #{}: IMPOSSIBLE".format(t))
                    break
                else:
                    Hd -= Ak
                    turns += 1
dragon_knight()