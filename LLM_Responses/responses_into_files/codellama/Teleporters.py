T = int(input())
for _ in range(T):
    N = int(input())
    Thundera = list(map(int, input().split()))
    Care_a_Lot = list(map(int, input().split()))
    teleporters = []
    for _ in range(N-2):
        teleporters.append(list(map(int, input().split())))
    
    min_teleportations = float('inf')
    for i in range(2**N):
        visited = [False] * (N+2)
        current_location = Thundera
        teleportation_count = 0
        
        for j in range(N-1):
            if ((current_location[0] - teleporters[i%N][0]) + 
                (current_location[1] - teleporters[i%N][1]) + 
                (current_location[2] - teleporters[i%N][2])) == 0:
                current_location = list(teleporters[i%N])
            visited[i%N] = True
            current_location = [x+y for x,y in zip(current_location,teleporters[(i+1)%N])]
            if current_location == Care_a_Lot:
                min_teleportations = min(min_teleportations, teleportation_count+1)
                break
        
    print("Case #{}: {}".format(_, "IMPOSSIBLE" if min_teleportations==float('inf') else str(min_teleportations)))