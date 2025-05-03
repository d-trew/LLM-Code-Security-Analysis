def fashion_show(N, M, pre_placed):
    points = [[0 for _ in range(N)] for _ in range(N)]
    placed = [[False for _ in range(N)] for _ in range(N)]
    
    # Calculate initial scores and mark already placed models
    for model in pre_placed:
        style, r, c = model
        points[r-1][c-1] += {'+': 1, 'x': 2}[style]
        placed[r-1][c-1] = True
    
    # Check rows and columns for legal placement of new models
    def is_legal(r, c):
        if any(placed[i][c-1] or points[i][c-1] > 0 for i in range(N)):
            return False
        if any(placed[r-1][j] or points[r-1][j] > 0 for j in range(N)):
            return False
        return True
    
    # Find best placement of new models
    def find_placement():
        max_point = 0
        max_style = ''
        max_pos = (-1, -1)
        
        for style in '+xo':
            for r in range(N):
                for c in range(N):
                    if not placed[r][c] and is_legal(r+1, c+1) and points[r][c] < (2 if style == 'o' else 1):
                        if max_point < (2 if style == 'o' else 1):
                            max_point = 2 if style == 'o' else 1
                            max_style = style
                            max_pos = (r, c)
        
        return max_style, max_pos[0]+1, max_pos[1]+1
    
    # Place new models and calculate total score
    def place_model():
        total = 0
        while True:
            style, r, c = find_placement()
            
            if style == '':
                break
                
            points[r-1][c-1] += {'+': 1, 'x': 2}[style]
            placed[r-1][c-1] = True
            total += 1
        
        return sum(sum(row) for row in points), total
    
    max_score, total_models = 0, 0
    for _ in range(M):
        score, models = place_model()
        if max_score < score:
            max_score, total_models = score, models
            
    return max_score, total_models