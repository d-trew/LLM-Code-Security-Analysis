import sys
input = sys.stdin.readlines

def min_coins(R, C, F, S):
    current = [list(map(str, input().strip())) for _ in range(R)]
    target = [list(map(str, input().strip())) for _ in range(R)]
    ops = 0

    for i in range(R):
        for j in range(C - 1):
            if current[i][j] != target[i][j] and current[i][j+1] == target[i][j]:
                current[i][j], current[i][j+1] = current[i][j+1], current[i][j]
                ops += S
                break
            if current[i][j] != target[i][j] and target[i][j+1] == current[i][j]:
                current[i][j], current[i][j+1] = current[i][j+1], current[i][j]
                ops += S
                break
            if current[i][j] != target[i][j] and current[i+1][j] == target[i][j]:
                current[i][j], current[i+1][j] = current[i+1][j], current[i][j]
                ops += S
                break
            if current[i][j] != target[i][j] and target[i+1][j] == current[i][j]:
                current[i][j], current[i+1][j] = current[i+1][j], current[i][j]
                ops += S
                break
        for j in range(C - 1, -1, -1):
            if current[i][j] != target[i][j] and current[i][j-1] == target[i][j]:
                current[i][j], current[i][j-1] = current[i][j-1], current[i][j]
                ops += S
                break
            if current[i][j] != target[i][j] and target[i][j-1] == current[i][j]:
                current[i][j], current[i][j-1] = current[i][j-1], current[i][j]
                ops += S
                break
            if current[i][j] != target[i][j] and current[i+1][j] == target[i][j]:
                current[i][j], current[i+1][j] = current[i+1][j], current[i][j]
                ops += S
                break
            if current[i][j] != target[i][j] and target[i+1][j] == current[i][j]:
                current[i][j], current[i+1][j] = current[i+1][j], current[i][j]
                ops += S
                break
    for i in range(R):
        for j in range(C):
            if current[i][j] != target[i][j]:
                if current[i][j] == 'M' and target[i][j] == 'G':
                    ops += F
                elif current[i][j] == 'G' and target[i][j] == 'M':
                    ops += F
    return ops

T = int(input().strip())
for t in range(1, T+1):
    R, C, F, S = map(int, input().split())
    print('Case #{}: {}'.format(t, min_coins(R, C, F, S)))