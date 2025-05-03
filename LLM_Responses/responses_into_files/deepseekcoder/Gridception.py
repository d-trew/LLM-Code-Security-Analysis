T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    dream_grid = [list(input()) for _ in range(R)]
    max_pattern_size = 0
    for pattern_size in range(1, min(R, C) + 1):
        for i in range(R - pattern_size + 1):
            for j in range(C - pattern_size + 1):
                if all(dream_grid[i+k][j+l] == dream_grid[i][j] for k in range(pattern_size) for l in range(pattern_size)):
                    max_pattern_size = max(max_pattern_size, pattern_size)
    print(f"Case # {_+1}: {max_pattern_size}")