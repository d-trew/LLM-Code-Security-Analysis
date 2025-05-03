import sys
input = sys.stdin.readlines

def min_leftovers(n, p, groups):
    leftover = 0
    people = sum(groups)
    max_new_packs = (people - 1) // p + 1
    if max_new_packs * p < people:
        return -1

    groups.sort()
    count = 0
    for group in groups:
        new_packs = min(max_new_packs, group)
        leftover += (group - new_packs) if leftover else 0
        max_new_packs -= new_packs

    return max_new_packs + (1 if leftover == 0 else 0)

T = int(input()[0])
for _ in range(T):
    n, p = map(int, input()[0].split())
    groups = list(map(int, input()[0].split()))
    print("Case #{}: {}".format(_ + 1, min_leftovers(n, p, groups)))