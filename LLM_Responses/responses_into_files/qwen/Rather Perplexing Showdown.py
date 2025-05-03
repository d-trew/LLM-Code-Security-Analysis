def generate_lineups(N, R, P, S):
    if (R == 0 or P == 0 or S == 0) and (R + P + S != 2 * N):
        return "IMPOSSIBLE"
    
    players = ['R'] * R + ['P'] * P + ['S'] * S
    lineups = []
    
    def backtrack(lineup):
        if len(lineup) == 2 * N:
            lineups.append(''.join(lineup))
            return
        
        for i in range(len(players)):
            if players[i] != 'X':
                new_lineup = lineup[:]
                new_lineup.append(players[i])
                players[i] = 'X'
                backtrack(new_lineup)
                players[i] = new_lineup[-1]

    backtrack([])
    
    valid_lineups = []
    for lineup in lineups:
        round_results = []
        for i in range(0, 2 * N, 2):
            if (lineup[i] == 'R' and lineup[i + 1] == 'S') or \
               (lineup[i] == 'S' and lineup[i + 1] == 'P') or \
               (lineup[i] == 'P' and lineup[i + 1] == 'R'):
                round_results.append('W')
            elif lineup[i] == lineup[i + 1]:
                round_results.append('T')
        
        if all(result != 'T' for result in round_results):
            valid_lineups.append(lineup)
    
    return sorted(valid_lineups)

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        R = int(data[index + 1])
        P = int(data[index + 2])
        S = int(data[index + 3])
        index += 4
        
        result = generate_lineups(N, R, P, S)
        if result == "IMPOSSIBLE":
            results.append(f"Case #{_+1}: IMPOSSIBLE")
        else:
            results.append(f"Case #{_+1}: {result[0]}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()