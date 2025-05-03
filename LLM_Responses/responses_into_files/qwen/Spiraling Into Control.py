def find_shortcuts(N, K):
    if N * N - 1 <= K:
        return "IMPOSSIBLE"
    
    center = N * N // 2 + 1
    moves = [0] * (N * N)
    x, y = 0, 0
    dx, dy = 0, 1
    
    for i in range(1, N * N):
        moves[i] = i
        if i % 2 == 0:
            dx, dy = -dy, dx
        
        while (x + dx < 0 or x + dx >= N) or (y + dy < 0 or y + dy >= N) or moves[moves[i]] != moves[i] + 1:
            dx, dy = -dy, dx
            if (x + dx < 0 or x + dx >= N) or (y + dy < 0 or y + dy >= N):
                return "IMPOSSIBLE"
        
        x += dx
        y += dy
    
    shortcuts = []
    for i in range(1, K + 2):
        if moves[i] != moves[i - 1] + 1:
            shortcuts.append((moves[i - 1], moves[i]))
    
    return len(shortcuts), shortcuts

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        result = find_shortcuts(N, K)
        if result == "IMPOSSIBLE":
            results.append(f"Case #{_+1}: IMPOSSIBLE")
        else:
            num_shortcuts, shortcuts = result
            results.append(f"Case #{_+1}: {num_shortcuts}")
            for a, b in shortcuts:
                results.append(f"{a} {b}")
    
    print("\n".join(results))

solve()