def solve():
    D, P = input().split()
    D = int(D)
    
    damage = 0
    strength = 1
    for instruction in P:
        if instruction == 'C':
            damage += strength
        else:
            strength *= 2
    
    if damage <= D:
        return 0
    
    hacks = 0
    
    while damage > D:
        last_c_index = -1
        for i in range(len(P) - 1):
            if P[i] == 'C' and P[i+1] == 'S':
                last_c_index = i
                break
        
        if last_c_index == -1:
            return "IMPOSSIBLE"

        P = list(P)
        P[last_c_index], P[last_c_index+1] = P[last_c_index+1], P[last_c_index]
        P = "".join(P)
        
        damage = 0
        strength = 1
        for instruction in P:
            if instruction == 'C':
                damage += strength
            else:
                strength *= 2
        hacks += 1

    return hacks

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")