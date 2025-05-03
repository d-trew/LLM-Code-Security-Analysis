def max_style_points(N, M, models):
    grid = [['.' for _ in range(N)] for _ in range(N)]
    
    def is_valid(r, c, model):
        if r != 1: return False
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.':
                    continue
                if (i == r and j == c) or (i == r and j != c) or (i != r and j == c) or (i + j == r + c) or (i - j == r - c):
                    if model == '+' and grid[i][j] not in ['+', 'x']:
                        return False
                    elif model == 'x' and grid[i][j] not in ['x', '+']:
                        return False
        return True
    
    for model, r, c in models:
        grid[r-1][c-1] = model
    
    added_or_substituted = 0
    style_points = 0
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.' and is_valid(i+1, j+1, 'o'):
                grid[i][j] = 'o'
                added_or_substituted += 1
                style_points += 2
            elif grid[i][j] == '+' and is_valid(i+1, j+1, 'x'):
                grid[i][j] = 'x'
                added_or_substituted += 1
                style_points += 1
            elif grid[i][j] == 'x' and is_valid(i+1, j+1, '+'):
                grid[i][j] = '+'
                added_or_substituted += 1
                style_points += 1
    
    result = []
    for i in range(N):
        for j in range(N):
            if (i+1, j+1) not in [(r, c) for _, r, c in models]:
                if grid[i][j] != '.':
                    result.append(f"{grid[i][j]} {i+1} {j+1}")
    
    return style_points, added_or_substituted, result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        models = [(data[index+2+3*i], int(data[index+3+3*i]), int(data[index+4+3*i])) for i in range(M)]
        index += 3 * (M + 1)
        
        style_points, added_or_substituted, result = max_style_points(N, M, models)
        results.append(f"Case #{_+1}: {style_points} {added_or_substituted}")
        results.extend(result)
    
    for line in results:
        print(line)

if __name__ == "__main__":
    main()