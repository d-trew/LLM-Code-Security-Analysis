from collections import deque

def can_assign_mascots(n, left_exits, right_exits):
    visited = [[False] * (n + 1) for _ in range(26)]
    current_room = [0]
    assigned_mascots = [''] * n

    while current_room:
        room = current_room.pop()
        for i in range(26):
            if ord('A') + i <= ord('M'):
                if not visited[i][room]:
                    if left_exits[room - 1] == room and chr(i + ord('A')) not in assigned_mascots[:room]:
                        visited[i][room] = True
                        current_room.append(left_exits[room - 1])
                        assigned_mascots[room - 1] = chr(i + ord('A'))
                    elif right_exits[room - 1] == room and chr(i + ord('A')) not in assigned_mascots[:room]:
                        visited[i][room] = True
                        current_room.append(right_exits[room - 1])
                        assigned_mascots[room - 1] = chr(i + ord('A'))
        if all(visited[i][n - 1] for i in range(26)):
            return ''.join(assigned_mascots)
    return 'IMPOSSIBLE'

T = int(input())
for t in range(T):
    n = int(input())
    left_exits = list(map(int, input().split()))
    right_exits = list(map(int, input().split()))
    print(f'Case #{t + 1}: {can_assign_mascots(n, left_exits, right_exits)}')