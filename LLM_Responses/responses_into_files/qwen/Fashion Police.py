T = int(input())
for _ in range(T):
    J, P, S, K = map(int, input().split())
    max_days = min(J, P)
    outfits = []
    for i in range(max_days):
        j, p = i % J + 1, i % P + 1
        s = (i // J) % S + 1
        outfits.append((j, p, s))
    print(f"Case # {_+1}: {max_days}")
    for outfit in outfits:
        print(*outfit)