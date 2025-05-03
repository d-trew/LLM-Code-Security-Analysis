from itertools import combinations

def count_decays(g):
    counts = [0] * (len(g) + 1)
    for digit in g:
        counts[int(digit)] += 1
    return ''.join(str(c) for c in counts)

def solve(G):
    decays = set()
    for length in range(1, len(G) + 1):
        for decay in combinations([count_decays(g) for g in decays], length):
            new_decay = ''.join(sorted(decay))
            if new_decay == count_decays(G):
                decays.add(G)
    return len(decays) if G in decays else float('inf')

T = int(input())
for _ in range(T):
    print(f'Case #{_+1}: {solve(input())}')


This code reads the number of test cases, T, and then iterates over each test case. For each test case, it calculates all possible decays for googlements of length 1 to the given length using combinations from previously calculated decays. If a new decay matches the given googlement, it is added to the set of decays. At the end, if the given googlement is in the set of decays, it returns the number of unique decays; otherwise, it returns 'inf'.