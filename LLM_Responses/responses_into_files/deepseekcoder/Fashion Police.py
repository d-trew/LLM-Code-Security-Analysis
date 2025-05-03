def fashion_jail(J, P, S, K):
    # Initialize the number of days and the list of outfits
    num_days = 0
    outfits = []
    
    # For each possible combination of jacket-pants-shirt
    for j in range(1, J+1):
        for p in range(j, P+1):
            for s in range(1, S+1):
                # Check if the number of combinations is less than K
                num_outfits = (J - j + 1) * (P - p + 1) * (S - s + 1)
                if num_outfits < K:
                    # Add the outfit to the list and increment the number of days
                    outfits.append((j, p, s))
                    num_days += 1
    
    return num_days, outfits

T = int(input())
for t in range(1, T+1):
    J, P, S, K = map(int, input().split())
    num_days, outfits = fashion_jail(J, P, S, K)
    
    print("Case #{}: {}".format(t, num_days))
    for outfit in outfits:
        print(*outfit)