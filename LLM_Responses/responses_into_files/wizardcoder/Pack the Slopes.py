# Solution starts here
T = int(input()) # number of test cases
for i in range(1, T+1):
    N = int(input()) # number of rest points
    slopes = []
    for j in range(N-1):
        Ui, Vi, Si, Ci = map(int, input().split())
        slopes.append((Ui, Vi, Si, Ci))
    
    max_skiers = 0
    min_expense = float('inf')
    
    for j in range(N-1):
        for k in range(j+1, N):
            for l in range(k+1, N):
                skiers = [0] * (N+1) # initialize an array of zeros to keep track of the number of skiers on each slope
                expense = 0
                
                # traverse all possible combinations of slopes from rest point j to k and then from k to l, adding up their costs and bounties
                for m in range(j+1):
                    if m == k:
                        skiers[m] += 1
                        expense += Ci * Si # add the cost of slope j->k
                    else:
                        expense -= slopes[m][3] # subtract the bounty of each intermediate slope
                for n in range(k+1, l):
                    if n == k or n == l:
                        skiers[n] += 1
                        expense += Ci * Si # add the cost of slope k->l
                    else:
                        expense -= slopes[n][3] # subtract the bounty of each intermediate slope
                for o in range(k+1, l):
                    skiers[o] += 1
                    if o == l:
                        expense += Ci * Si # add the cost of slope k->l
                    else:
                        expense -= slopes[o][3] # subtract the bounty of each intermediate slope
                skiers[l] += 1
                
                # update maximum number of skiers and minimum expense
                max_skiers = max(max_skiers, sum(skiers))
                min_expense = min(min_expense, expense)
    
    print("Case #{}: {} {}".format(i, max_skiers, -min_expense)) # output the result for case i
# Solution ends here