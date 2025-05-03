from collections import deque

def solve_case(n, m, preplaced_models):
    max_style = 0
    best_solution = []
    
    for _ in range(4**m):
        current_models = [0] * (n * n)
        for model in preplaced_models:
            current_models[model[1]*n+model[0]] = model[2]
        
        visited = set()
        queue = deque([(0, 0, 0)])
        while queue:
            x, y, style = queue.popleft()
            if (x, y) not in visited:
                visited.add((x, y))
                current_style = style
                if current_models[x*n+y] == '+':
                    current_style += 1
                elif current_models[x*n+y] == 'x':
                    current_style += 1
                elif current_models[x*n+y] == 'o':
                    current_style += 2
                
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                        queue.append((nx, ny, current_style))
                
                if len(visited) == n * n:
                    max_style = max(max_style, current_style)
                    best_solution = [(i*n+j, 'o' if current_models[i*n+j] == '+' else ('x' if current_models[i*n+j] == 'x' else '.'), i+1, j+1) for i in range(n) for j in range(n) if (i, j) not in visited and current_models[i*n+j] != 'o']
    
    return max_style, len(best_solution)

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    preplaced_models = []
    for _ in range(m):
        x, y, model_type = input().split()
        x, y = int(x), int(y)
        if model_type == '+':
            model_type = 'o'
        elif model_type == 'x':
            model_type = 'o'
        preplaced_models.append((y, x, model_type[0]))
    style, added_models = solve_case(n, m, preplaced_models)
    print(f"Case #{t}: {style} {len(added_models)}")
    for model in added_models:
        print(*model)