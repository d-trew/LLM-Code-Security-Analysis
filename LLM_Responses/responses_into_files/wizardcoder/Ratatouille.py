import sys
sys.setrecursionlimit(10**6)
def is_valid_kit(ingredients):
    total = sum([x[0] * x[1] for x in ingredients])
    return all(90 <= (x[0] / total * 100) <= 110 and 90 <= (x[1] / total * 100) <= 100 for x in ingredients)

def count_valid_kits(ingredients, used=set()):
    if len(used) == len(ingredients):
        return [[]]
    kits = []
    for i in range(len(ingredients)):
        if i not in used:
            new_used = set(used) | {i}
            kit = count_valid_kits(ingredients, new_used)
            kits.extend([[ingredients[i]] + x for x in kit])
    return kits

def max_valid_kits(ingredients):
    valid_kits = [kit for kit in count_valid_kits(ingredients) if is_valid_kit(kit)]
    return len(valid_kits)

T = int(input())
for i in range(1, T + 1):
    N, P = map(int, input().split())
    ingredients = []
    for _ in range(N):
        R, Q = map(int, input().split())
        ingredients.append((R, Q))
    print("Case #%d: %d" % (i, max_valid_kits(ingredients)))