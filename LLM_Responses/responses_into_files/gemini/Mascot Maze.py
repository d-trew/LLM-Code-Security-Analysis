def solve():
    N = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    
    mascots = "ACDEHIJKMORST"
    
    def is_valid(assignment):
        for i in range(N):
            for j in range(2):
                curr = i + 1
                path = [curr]
                next_room = L[i] if j == 0 else R[i]
                path.append(next_room)
                
                if len(path) >=3:
                  
                    for k in range(len(path) -2):
                        if assignment[path[k]-1] == assignment[path[k+1]-1] or assignment[path[k]-1] == assignment[path[k+2]-1] or assignment[path[k+1]-1] == assignment[path[k+2]-1]:
                            return False
                
                
                
                while True:
                    
                    next_room_l = L[next_room -1]
                    next_room_r = R[next_room -1]
                    
                    if len(path) >=3:
                      if assignment[path[-3]-1] == assignment[path[-2]-1] or assignment[path[-3]-1] == assignment[path[-1]-1] or assignment[path[-2]-1] == assignment[path[-1]-1]:
                        return False
                    
                    
                    if next_room_l in path and next_room_r in path:
                        break
                    
                    next_room = next_room_l if next_room_l not in path else next_room_r
                    
                    path.append(next_room)
                    

                    if len(path) > N:
                        break
                    
                    
                        
                    
                    
        return True

    import itertools
    
    for assignment_tuple in itertools.product(mascots, repeat=N):
        assignment = "".join(assignment_tuple)
        if is_valid(assignment):
            return assignment
    return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")