T = int(input())
for _ in range(T):
    hd, ad, hk, ak, b, d = map(int, input().split())
    if (hk - ad) // d > 0:
        print(f"Case # {_+1}: IMPOSSIBLE")
    else:
        turns = 0
        while hd > 0 and hk > 0:
            turns += 1
            hk -= max(0, ad)
            ad += b
            if ak - d > 0:
                hd -= min(hd, ak - d)
            else:
                hd -= ak
            if hd <= 0 or hk <= 0:
                break
        print(f"Case # {_+1}: {turns}")