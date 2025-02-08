def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()

    max_prob = 0

    for i in range(1, K + 2):
        for j in range(i, K + 2):
            win_count = 0
            for c in range(1, K + 1):
                min_dist = float('inf')
                min_dist_count = 0

                for p in P:
                    dist = abs(c - p)
                    if dist < min_dist:
                        min_dist = dist
                        min_dist_count = 1
                    elif dist == min_dist:
                        min_dist_count +=1

                dist1 = abs(c - i)
                dist2 = abs(c - j)

                if dist1 < min_dist or (dist1 == min_dist and min_dist_count ==1 and dist2 <= min_dist):
                    win_count +=1
                elif dist2 < min_dist or (dist2 == min_dist and min_dist_count ==1 and dist1 <=min_dist):
                    win_count +=1


            max_prob = max(max_prob, win_count / K)

    return max_prob

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")