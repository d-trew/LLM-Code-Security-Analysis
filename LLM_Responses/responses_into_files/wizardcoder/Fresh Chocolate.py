T = int(input())
for i in range(1, T+1):
    N, P = map(int, input().split())
    groups = list(map(int, input().split()))
    
    leftovers = 0
    fresh_groups = 0
    for group in sorted(groups, reverse=True):
        if leftovers >= group:
            fresh_groups += 1
            leftovers -= group
        else:
            leftovers = P - (group % P)
    
    print("Case #%d: %d" % (i, fresh_groups))