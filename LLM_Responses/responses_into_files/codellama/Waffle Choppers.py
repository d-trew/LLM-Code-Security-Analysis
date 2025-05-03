T = int(input())
for _ in range(T):
    R, C, H, V = [int(x) for x in input().split()]
    waffle = [input() for _ in range(R)]
    chocolate_count = sum(1 for row in waffle for cell in row if cell == '@')
    pieces = {}
    for i in range(H + 1):
        for j in range(V + 1):
            piece = ''
            for k in range(R):
                for l in range(C):
                    if k < R - 1 and (i == H or k >= i):
                        piece += waffle[k][l]
                    else:
                        break
            for l in range(C):
                if l < C - 1 and (j == V or l >= j):
                    piece += waffle[R - 1][l]
                else:
                    break
            pieces.setdefault(tuple(map(len, piece.split('.'))), []).append(piece)
    for x in pieces.values():
        if len(set(x)) > 1:
            print('Case #{}: IMPOSSIBLE'.format(_ + 1))
            break
    else:
        print('Case #{}: POSSIBLE'.format(_ + 1))