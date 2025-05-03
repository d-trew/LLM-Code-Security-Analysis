import sys
T = int(input())
for i in range(1, T+1):
    D, P = input().split()
    D = int(D)
    S = ''.join([P[i] for i in range(len(P)) if P[i] == 'S'])
    C = ''.join([P[i] for i in range(len(P)) if P[i] == 'C'])
    hacks_needed = 0
    
    # If there are no S's or the shield can withstand all damage, output "IMPOSSIBLE"
    if len(S) == 0 or D >= len(P):
        print("Case #{}: IMPOSSIBLE".format(i))
    
    # Otherwise, count how many hacks are needed to reduce the damage to the maximum possible withstandable amount
    else:
        for j in range(len(S)-1):
            if P.count('SC', j, j+2) > 0:
                hacks_needed += 1
        
        # If there are no adjacent pairs of S and C to swap, output the number of hacks needed
        if hacks_needed == len(S):
            print("Case #{}: {}".format(i, hacks_needed))
        else:
            # If it is not possible to reduce damage to within the shield's limit, output "IMPOSSIBLE"
            print("Case #{}: IMPOSSIBLE".format(i))