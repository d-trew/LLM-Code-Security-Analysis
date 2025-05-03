def place_unicorns(N, R, O, Y, G, B, V):
    if N == 0:
        return "IMPOSSIBLE"
    
    # Create a list of colors based on the number of unicorns with each color mane
    colors = ['R'] * R + ['O'] * O + ['Y'] * Y + ['G'] * G + ['B'] * B + ['V'] * V
    
    # Check if it's possible to arrange the unicorns in a circle
    for i in range(N):
        valid = True
        for j in range(1, N):
            if colors[(i + j) % N] == colors[(i - j) % N]:
                valid = False
                break
        if valid:
            return ''.join(colors[i:] + colors[:i])
    
    return "IMPOSSIBLE"

# Read input
T = int(input())
results = []
for t in range(1, T + 1):
    N, R, O, Y, G, B, V = map(int, input().split())
    results.append(f"Case #{t}: {place_unicorns(N, R, O, Y, G, B, V)}")

# Print all results
for result in results:
    print(result)