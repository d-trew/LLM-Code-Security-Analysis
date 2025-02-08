def solve():
    N = int(input())
    holes = []
    for _ in range(N):
        holes.append(list(map(int, input().split())))

    max_holes_touched = 0

    for i in range(1 << (N * (N - 1) // 2)):
        wormholes = []
        k = i
        edges = []
        for u in range(N):
            for v in range(u + 1, N):
                if k % 2 == 1:
                    edges.append((u, v))
                k //= 2

        for start_hole in range(N):
            for end_hole in range(N):
                if start_hole == end_hole:
                    continue

                #Simulate ball trajectory
                touched_holes = set()
                current_hole = start_hole
                
                dx = holes[end_hole][0] - holes[start_hole][0]
                dy = holes[end_hole][1] - holes[start_hole][1]

                
                while True:
                    touched_holes.add(current_hole)
                    next_hole = -1
                    min_dist = float('inf')

                    for j in range(N):
                        if j == current_hole:
                            continue
                        
                        dist = (holes[j][0] - holes[current_hole][0])*dy - (holes[j][1]-holes[current_hole][1])*dx
                        if abs(dist) < 1e-6 and (holes[j][0]-holes[current_hole][0]) * dx >=0 and (holes[j][1]-holes[current_hole][1]) * dy >=0:
                            
                            d = (holes[j][0] - holes[current_hole][0])**2 + (holes[j][1] - holes[current_hole][1])**2
                            if d < min_dist:
                                min_dist = d
                                next_hole = j

                    if next_hole == -1:
                        break
                    
                    current_hole = next_hole
                    
                    
                    for u,v in edges:
                        if current_hole == u:
                            current_hole = v
                            break
                        elif current_hole == v:
                            current_hole = u
                            break


                max_holes_touched = max(max_holes_touched, len(touched_holes))

    return max_holes_touched


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")