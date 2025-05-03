import itertools

def solve(N, R, P, S):
    players = list('RPS' * N)
    for perm in itertools.permutations(players):
        if not any(perms == ['RR', 'SS', 'PP'] for perms in list(itertools.combinations(perm, 2))):
            return "IMPOSSIBLE"
        else:
            perm_str = ''.join(sorted(perm))
            if not solve(N - 1, R - (perm.count('R') - 1), P - (perm.count('P') - 1), S - (perm.count('S') - 1)):
                return perm_str
    return "IMPOSSIBLE"

def main():
    T = int(input())
    for t in range(T):
        N, R, P, S = map(int, input().split())
        print(f"Case #{t+1}: {solve(N, R, P, S)}")

main()