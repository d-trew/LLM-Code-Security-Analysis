import sys
input = sys.stdin.readline

def can_win(n, cards):
    card_dict = {}
    for c in cards:
        value, suit = c[0], c[1]
        if value not in card_dict:
            card_dict[value] = []
        card_dict[value].append((suit, len(card_dict[value])))

    moves = set()
    for v in card_dict.keys():
        suits = [c[0] for c in card_dict[v]]
        if len(suits) > 1:
            moves |= {s for s in suits if (v, s) not in moves}

    return len(moves) >= n - 1 and all([len(card_dict[v]) <= 1 for v in card_dict.keys()])

T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    cards = []
    for _ in range(N):
        c_count, data = map(int, input().split())
        cards.append([(c_count, s) for s in [input().split() for _ in range(c_count)]])

    print('Case #{}: {}'.format(_ + 1, 'POSSIBLE' if can_win(N, cards) else 'IMPOSSIBLE'))