import itertools
from collections import Counter

def rock_paper_scissors(N):
    lineups = []
    for r in range(1, N+1):
        for p in range(1, N-r+1):
            s = N - r - p
            if s > 0:
                lineup = ''.join(['R']*r + ['P']*p + ['S']*s)
                lineups.append(''.join([lineup[::2], lineup[1::2]]))
    return sorted(lineups)

T = int(input())
for i in range(1, T+1):
    N, R, P, S = map(int, input().split())
    
    if (R + P + S) % 2 != 0:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        lineups = rock_paper_scissors(N)
        
        if len(lineups) == 0:
            print("Case #{}: IMPOSSIBLE".format(i))
        else:
            sorted_lineup = min(lineups, key=Counter)
            print("Case #{}: {}".format(i, sorted_lineup[::-1]) if (R >= P and S >= R) or (P >= R and S >= P) else "Case #{} IMPOSSIBLE".format(i))