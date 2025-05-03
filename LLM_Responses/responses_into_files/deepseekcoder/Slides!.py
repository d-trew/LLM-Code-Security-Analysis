T = int(input())
for t in range(1, T+1):
    B, M = map(int, input().split())
    if M % (B-1) != 0:
        print(f"Case #{t}: IMPOSSIBLE")
    else:
        slides = [[0]*B for _ in range(B)]
        for _ in range(M//((B-1))):
            start, end = map(int, input().split())
            if start == B:
                break
            if start < end:
                slides[start][end] = 1
            else:
                slides[end][start] = 1
        print(f"Case #{t}: POSSIBLE")
        for i in range(B-1):
            for j in range(i+1, B):
                if (M//((B-1))) % 2 == 0:
                    slides[i+1][j] = 1
                else:
                    slides[i][j] = 1
        for row in slides:
            print(' '.join(str(cell) for cell in row))