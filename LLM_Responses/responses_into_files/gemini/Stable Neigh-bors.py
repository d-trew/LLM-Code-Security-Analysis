def solve():
    N, R, O, Y, G, B, V = map(int, input().split())

    colors = {'R': R, 'O': O, 'Y': Y, 'G': G, 'B': B, 'V': V}
    
    adj = {
        'R': ['O', 'V'],
        'O': ['R', 'Y'],
        'Y': ['O', 'G'],
        'G': ['Y', 'B'],
        'B': ['G', 'V'],
        'V': ['R', 'B']
    }

    def is_valid(arrangement):
        for i in range(N):
            if arrangement[i] in adj[arrangement[(i + 1) % N]] or arrangement[(i + 1) % N] in adj[arrangement[i]]:
                return False
        return True

    import itertools
    
    
    all_unicorns = []
    for color, count in colors.items():
        all_unicorns.extend([color] * count)

    for arrangement in itertools.permutations(all_unicorns):
        if is_valid(list(arrangement)):
            return "".join(arrangement)

    return "IMPOSSIBLE"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")