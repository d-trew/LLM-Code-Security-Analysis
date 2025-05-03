def is_valid_move(r1, c1, r2, c2):
    return abs(r1 - r2) != 0 and abs(c1 - c2) != 0 and abs(r1 - r2) != abs(c1 - c2)

def solve(R, C):
    if R == 1 and C == 1:
        return "IMPOSSIBLE"
    
    start = (R // 2 + 1, C // 2 + 1)
    path = [start]
    
    for _ in range(R * C - 1):
        r, c = path[-1]
        found = False
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 1 <= nr <= R and 1 <= nc <= C and (nr, nc) not in path:
                    found = True
                    path.append((nr, nc))
                    break
            if found:
                break
        if not found:
            return "IMPOSSIBLE"
    
    result = []
    for r, c in path:
        result.append(f"{r} {c}")
    
    return "\n".join(result)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        R = int(data[index])
        C = int(data[index + 1])
        index += 2
        result = solve(R, C)
        results.append(result)
    
    for i, res in enumerate(results, start=1):
        print(f"Case #{i}: {res}")

if __name__ == "__main__":
    main()