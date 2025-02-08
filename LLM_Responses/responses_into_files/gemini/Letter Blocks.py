import itertools

def solve():
    N = int(input())
    towers = [input() for _ in range(N)]

    for perm in itertools.permutations(towers):
        megatower = "".join(perm)
        valid = True
        letters = set(list(megatower))
        for letter in letters:
            indices = [i for i, x in enumerate(megatower) if x == letter]
            if len(indices) > 1:
                for i in range(len(indices) - 1):
                    for j in range(indices[i] + 1, indices[i+1]):
                        if megatower[j] != letter:
                            valid = False
                            break
                    if not valid:
                        break
            if not valid:
                break
        if valid:
            return megatower
    return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")