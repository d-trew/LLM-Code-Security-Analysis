def rps_tournament(n, r, p, s):
    if (r + p + s) != 2 * n or min([r, p, s]) < 1 or max([r, p, s]) > 2 * n:
        return "IMPOSSIBLE"
    
    players = ['R'*r + 'P'*p + 'S'*s]
    while len(players[0]) > 2:
        new_lineup = ""
        for i in range(len(players[0]) // 2):
            if (players[0][i*2] == "R" and players[0][i*2+1] == "P") or \
               (players[0][i*2] == "P" and players[0][i*2+1] == "S") or \
               (players[0][i*2] == "S" and players[0][i*2+1] == "R"):
                new_lineup += 'P' if players[0][i*2] in ('R', 'S') else 'R'
            elif players[0][i*2] == players[0][i*2+1]:
                return "IMPOSSIBLE"
            else:
                new_lineup += 'S' if (players[0][i*2] in ('P', 'R') or players[0][i*2+1] in ('P', 'R')) else 'P'
        players = [new_lineup] + players
    return players[0]

T = int(input())
for t in range(1, T + 1):
    N, R, P, S = map(int, input().split())
    print("Case #{}: {}".format(t, rps_tournament(N, R, P, S)))