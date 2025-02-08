def solve():
    N, R, P, S = map(int, input().split())
    
    total_players = 2**N
    if R + P + S != total_players:
        return "IMPOSSIBLE"

    def check_lineup(lineup):
        current_lineup = list(lineup)
        while len(current_lineup) > 1:
            next_lineup = []
            for i in range(0, len(current_lineup), 2):
                player1 = current_lineup[i]
                player2 = current_lineup[i+1]
                if (player1 == 'R' and player2 == 'S') or \
                   (player1 == 'S' and player2 == 'P') or \
                   (player1 == 'P' and player2 == 'R'):
                    next_lineup.append(player1)
                elif (player2 == 'R' and player1 == 'S') or \
                     (player2 == 'S' and player1 == 'P') or \
                     (player2 == 'P' and player1 == 'R'):
                    next_lineup.append(player2)
                else:
                    return False
            current_lineup = next_lineup
        return True

    import itertools
    
    lineup_template = [''] * total_players
    
    for i in range(R):
        lineup_template[i] = 'R'
    for i in range(R, R+P):
        lineup_template[i] = 'P'
    for i in range(R+P, total_players):
        lineup_template[i] = 'S'

    
    valid_lineups = []
    for lineup in itertools.permutations(lineup_template):
        if check_lineup("".join(lineup)):
            valid_lineups.append("".join(lineup))

    if valid_lineups:
        valid_lineups.sort()
        return valid_lineups[0]
    else:
        return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")