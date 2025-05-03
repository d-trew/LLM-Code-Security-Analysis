def min_hacks(D, P):
    damage = 0
    max_damage = D
    hack_count = 0
    P += 'C'
    
    for i in range(len(P) - 1):
        if P[i] == 'S':
            damage += 1
            if damage > max_damage:
                return "IMPOSSIBLE"
        else: # P[i] == 'C'
            if P[i+1] == 'S':
                hack_count += 1
                damage -= 1
            elif P[i-1] == 'S':
                continue
            else: 
                return "IMPOSSIBLE"
    
    while damage < max_damage:
        if hack_count == 0:
            return "IMPOSSIBLE"
        hack_count -= 1
        damage += 1
        
    return hack_count

T = int(input())
for t in range(T):
    D, P = input().split()
    print("Case #{}: {}".format(t+1, min_hacks(int(D), P)))