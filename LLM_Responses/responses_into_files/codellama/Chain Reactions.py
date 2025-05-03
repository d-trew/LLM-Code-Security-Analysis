# Test cases
T = int(input())
for t in range(1, T+1):
    N = int(input())
    F = list(map(int, input().split()))
    P = list(map(int, input().split()))
    
    # Compute the maximum fun Wile can get by manually triggering the initiators in the best possible order
    max_fun = 0
    for i in range(N):
        if P[i] == 0:
            continue
        else:
            module = i + 1
            chain_reaction = []
            while module != 0:
                chain_reaction.append(F[module])
                module = P[module]
            max_fun = max(max_fun, max(chain_reaction))
    
    print("Case #" + str(t) + ": " + str(max_fun))