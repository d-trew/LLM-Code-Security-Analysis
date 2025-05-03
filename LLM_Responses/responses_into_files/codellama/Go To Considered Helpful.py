# Test cases
T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    matrix = []
    for i in range(R):
        matrix.append([])
        for j in range(C):
            matrix[i].append(input()[j])
    # Find Marlin and his son's positions
    marlin_row, marlin_col = -1, -1
    son_row, son_col = -1, -1
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 'M':
                marlin_row, marlin_col = i, j
            elif matrix[i][j] == 'N':
                son_row, son_col = i, j
    # Find the shortest path from Marlin to his son
    visited = set()
    queue = [(marlin_row, marlin_col)]
    while queue:
        row, col = queue.pop(0)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < R and 0 <= new_col < C and matrix[new_row][new_col] not in ['#', 'M'] and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                if new_row == son_row and new_col == son_col:
                    break
        else:
            continue
        break
    # Print the shortest path
    print('Case #{}: {}'.format(t+1, len(queue)))