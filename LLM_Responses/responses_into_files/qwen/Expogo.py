def expogo_stick_jumps(X, Y):
    if X == 0 and Y == 0:
        return "IMPOSSIBLE"
    
    jumps = []
    distance = abs(X) + abs(Y)
    
    for i in range(1, distance // 2 + 1):
        if 2 * (i - 1) >= abs(X) or 2 * (i - 1) >= abs(Y):
            break
        if X > 0:
            jumps.append("E")
            X -= 2 * (i - 1)
        elif X < 0:
            jumps.append("W")
            X += 2 * (i - 1)
        if Y > 0:
            jumps.append("N")
            Y -= 2 * (i - 1)
        elif Y < 0:
            jumps.append("S")
            Y += 2 * (i - 1)
    
    if X != 0 or Y != 0:
        return "IMPOSSIBLE"
    
    return "".join(jumps)

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, len(data), 2):
        X = int(data[i])
        Y = int(data[i + 1])
        result = expogo_stick_jumps(X, Y)
        results.append(f"Case #{i // 2 + 1}: {result}")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()