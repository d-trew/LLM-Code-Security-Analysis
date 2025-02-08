def solve():
    N, K = map(int, input().split())
    
    if K < N or K > (N*N -1):
        return "IMPOSSIBLE"

    shortcuts = []
    current_room = 1
    moves_left = K
    
    while current_room < N*N:
        next_room = current_room + 1
        moves_left -=1
        
        if moves_left == 0 and next_room != N*N:
            return "IMPOSSIBLE"
            
        if next_room == N*N:
            break
        
        if moves_left > 0:
            jump_size = min(N -1, moves_left)
            next_room = current_room + 1 + jump_size
            if next_room <= N * N:
                shortcuts.append((current_room+1,next_room))
                moves_left -= jump_size
                current_room = next_room
                
            else:
                return "IMPOSSIBLE"
        
        current_room = next_room
        

    return len(shortcuts), shortcuts


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}:")
    if isinstance(result, str):
        print(result)
    else:
        num_shortcuts, shortcut_list = result
        print(num_shortcuts)
        for shortcut in shortcut_list:
            print(shortcut[0], shortcut[1])