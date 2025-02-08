def solve():
    R, C = map(int, input().split())
    matrix = [input() for _ in range(R)]

    def is_connected(matrix, char):
        visited = [[False for _ in range(C)] for _ in range(R)]
        q = []
        
        found_start = False
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == char:
                    q.append((r,c))
                    visited[r][c] = True
                    found_start = True
                    break
            if found_start:
                break

        if not found_start:
            return True

        count = 0
        while q:
            r, c = q.pop(0)
            count +=1
            
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] == char and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
        
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == char and not visited[r][c]:
                    return False
        return True

    
    def check_solution(connections):
        new_matrix = [list(row) for row in matrix]
        for r in range(R - 1):
            for c in range(C - 1):
                if connections[r][c] == '\\':
                    new_matrix[r][c] += 'x'
                    new_matrix[r+1][c+1] +='x'
                    
                elif connections[r][c] == '/':
                    new_matrix[r+1][c] +='x'
                    new_matrix[r][c+1] +='x'

        
        adj_a = {}
        adj_b = {}
        for r in range(R):
            for c in range(C):
                char = new_matrix[r][c][0]
                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<R and 0<=nc<C and new_matrix[nr][nc][0] == char:
                        if char=='A':
                            adj_a[(r,c)] = adj_a.get((r,c),[]) + [(nr,nc)]
                        else:
                            adj_b[(r,c)] = adj_b.get((r,c),[]) + [(nr,nc)]


                for dr, dc in [(1,1),(-1,-1), (1,-1),(-1,1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<R and 0<=nc<C and new_matrix[nr][nc][0] == char:
                        if new_matrix[r][c][-1] == 'x' and new_matrix[nr][nc][-1] == 'x':
                            if char=='A':
                                adj_a[(r,c)] = adj_a.get((r,c),[]) + [(nr,nc)]
                            else:
                                adj_b[(r,c)] = adj_b.get((r,c),[]) + [(nr,nc)]


        return is_connected(new_matrix, 'A') and is_connected(new_matrix, 'B')


    for i in range(3**(R*(C-1))):
        temp = i
        connections = [['.' for _ in range(C - 1)] for _ in range(R - 1)]
        for r in range(R - 1):
            for c in range(C - 1):
                val = temp % 3
                temp //= 3
                if val == 0:
                    connections[r][c] = '.'
                elif val == 1:
                    connections[r][c] = '\\'
                else:
                    connections[r][c] = '/'
        if check_solution(connections):
            print("POSSIBLE")
            for row in connections:
                print("".join(row))
            return

    print("IMPOSSIBLE")

T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: ", end="")
    solve()