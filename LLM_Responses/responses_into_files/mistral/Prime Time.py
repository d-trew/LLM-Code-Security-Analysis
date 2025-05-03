from math import isprime
import sys
input = sys.stdin.readlines

def is_valid(cards, group1, group2):
    return sum(group1) == (1 if len(group2) == 1 else prod(group2))

def prod(nums):
    return reduce(lambda a, b: a * b, nums)

def split_deck(cards):
    groups = [[], []]
    for card in cards:
        if not groups[0]:
            groups[0].append(card)
        elif is_valid(cards, groups[0], groups[1] + [card]):
            groups[1].append(card)
        else:
            groups[0].append(card)
    return max([sum(group) for group in groups]) if groups[0] else 0

T = int(input().strip())
for t in range(1, T+1):
    M = int(input().strip())
    cards = []
    for _ in range(M):
        p, n = map(int, input().split())
        cards += [(p, n) for _ in range(n)]
    print('Case #{}: {}'.format(t, split_deck(cards)))