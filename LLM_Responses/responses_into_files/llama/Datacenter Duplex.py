T = int(input())
for t in range(1, T+1):
    R, C = map(int, input().split())
    G = [list(input()) for _ in range(R)]
    As = [(i, j) for i in range(R) for j in range(C) if G[i][j] == 'A']
    Bs = [(i, j) for i in range(R) for j in range(C) if G[i][j] == 'B']
    print(f'Case #{t}:', end=' ')
    if not solve(G, As, Bs):
        print('IMPOSSIBLE')
    else:
        print('POSSIBLE')
        for row in G:
            line = ''
            for cell in row:
                if (cell == 'A' and any(neighbor == 'A' or neighbor == '.' for neighbor in [(i, j) if abs(i-j) == 1] + [(i-1, j) if i > 0] + [(i+1, j) if i < R-1] + [(i, j-1) if j > 0] + [(i, j+1) if j < C-1])):
                    line += '/'
                elif (cell == 'B' and any(neighbor == 'B' or neighbor == '.' for neighbor in [(i, j) if abs(i-j) == 1] + [(i-1, j) if i > 0] + [(i+1, j) if i < R-1] + [(i, j-1) if j > 0] + [(i, j+1) if j < C-1])):
                    line += '\\'
                else:
                    line += cell
            print(line)