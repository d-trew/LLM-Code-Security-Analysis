import math

def fractal_artwork(K, C):
    artwork = "L" * K + "G" * (math.pow(2, C) - 1) * K + "L" * K
    return artwork[:K]

T = int(input())
for i in range(1, T+1):
    K, C, S = map(int, input().split())
    if S >= K:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        tiles_to_clean = list(range(1, min(S+1) + 1))
        print("Case #{}: {}".format(i, " ".join(map(str, tiles_to_clean)))<|im_sep|>