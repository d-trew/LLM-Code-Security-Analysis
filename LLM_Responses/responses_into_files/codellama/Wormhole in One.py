T = int(input())
for _ in range(T):
    N = int(input())
    holes = []
    for _ in range(N):
        x, y = map(int, input().split())
        holes.append((x, y))
    
    max_holes = 0
    for i in range(len(holes)):
        for j in range(i+1, len(holes)):
            distance = ((holes[i][0]-holes[j][0])**2 + (holes[i][1]-holes[j][1])**2)**0.5
            if distance == int(distance):
                holes[i] += (j,)
                holes[j] += (i,)
    
    for i in range(len(holes)):
        for hole in holes[i]:
            if not isinstance(hole, tuple):
                max_holes = max(max_holes, 1)
            else:
                for h in hole:
                    if not isinstance(h, tuple):
                        max_holes = max(max_holes, 1)
    
    print(f"Case #{_+1}: {max_holes}")