def solve():
    N, P = map(int, input().split())
    opponents = []
    for i in range(N):
        attacks, defenses = map(int, input().split())
        opponent_attacks = list(map(int, input().split()))
        opponent_defenses = list(map(int, input().split()))
        opponents.append((opponent_attacks, opponent_defenses))

    return "YES" if can_win(opponents, P) else "NO"

def can_win(opponents, P):
    # This is a simplified solution that doesn't handle all cases correctly.
    # A complete solution would require a more sophisticated game-theoretic approach.

    # Check if any opponent knows all defenses.  If so, we can't guarantee victory.
    for attacks, defenses in opponents:
        if len(set(defenses)) == P:
            return False

    return True


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")