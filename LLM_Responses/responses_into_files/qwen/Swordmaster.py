def can_become_swordmaster(test_cases):
    results = []
    for i in range(1, test_cases + 1):
        n, p = map(int, input().split())
        known_attacks = set([1])
        known_defenses = set([1])
        
        opponents = [set() for _ in range(n)]
        for j in range(n):
            attacks, defenses = map(int, input().split())
            for k in range(attacks):
                a = int(input())
                known_attacks.add(a)
                opponents[j].add((a, 0))
            for k in range(defenses):
                d = int(input())
                known_defenses.add(d)
                opponents[j].add((0, d))
        
        can_win = True
        for j in range(n):
            if not any(opponent[1] == 0 for opponent in opponents[j]):
                can_win = False
                break
        
        results.append("Case #" + str(i) + ": " + ("YES" if can_win else "NO"))
    
    return results

# Example usage:
test_cases = int(input())
results = can_become_swordmaster(test_cases)
for result in results:
    print(result)