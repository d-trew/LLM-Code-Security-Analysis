from itertools import combinations, permutations

def mine_hexacoins(N, D, S, E, L):
    pairs = list(combinations(L, 2))
    sums = [sum(map(int, list(x), base=D) % (16 * (10 ** (D - 1)))) for x in pairs]
    valid_sums = [x for x in sums if S <= x <= E]
    probability = len(valid_sums) / (combinations(L, D) * (D - 1))
    return probability

T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    S, E = input().split()
    L = list(map(str, input().split()))
    print("Case #{}: {}/{}".format(_ + 1, mine_hexacoins(N, D, S, E, L), len(combinations(L, D))))