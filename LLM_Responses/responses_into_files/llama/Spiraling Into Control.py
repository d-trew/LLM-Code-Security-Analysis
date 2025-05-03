T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    if N % 2 == 0:
        print(f"Case #{t}: IMPOSSIBLE")
    else:
        x, y = 1, 1
        shortcuts = []
        while K > 0 and y < N*N:
            if (x+y) % N == 0 or (x+y+1) % N == 0:
                y += 2
                K -= 1
            else:
                if x + 1 < N * N // N:
                    x += 1
                else:
                    x, y = x + N - 1, y + 1
                shortcuts.append((x, y))
        if K > 0:
            print(f"Case #{t}: IMPOSSIBLE")
        else:
            print(f"Case #{t}: {len(shortcuts)}")
            for i in range(len(shortcuts)):
                print(*shortcuts[i], sep=' ')