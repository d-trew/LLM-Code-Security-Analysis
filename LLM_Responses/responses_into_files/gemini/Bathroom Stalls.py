def solve():
    n, k = map(int, input().split())

    stalls = [(n + 2, 0, 0)]  # (length, min_dist, max_dist)
    
    for _ in range(k):
        stalls.sort(reverse=True)
        length, min_dist, max_dist = stalls.pop(0)
        
        if length == 1:
          break
        
        max_dist_new = (length - 1) // 2
        min_dist_new = (length - 1) // 2
        
        if (length -1) % 2 == 0:
            stalls.append(((length - 1) // 2 , min_dist_new, max_dist_new))
            stalls.append(((length - 1) // 2, min_dist_new, max_dist_new))
        else:
            stalls.append(((length - 1) // 2, min_dist_new, max_dist_new))
            stalls.append(((length - 1) // 2 +1, min_dist_new, max_dist_new+1))
            

    stalls.sort(reverse=True)
    return stalls[0][2], stalls[0][1]


t = int(input())
for i in range(1, t + 1):
    max_dist, min_dist = solve()
    print(f"Case #{i}: {max_dist} {min_dist}")