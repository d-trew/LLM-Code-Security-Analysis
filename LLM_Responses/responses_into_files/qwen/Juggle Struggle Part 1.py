def find_magnificent_arrangement(N, positions):
    pairs = []
    for i in range(0, 2*N, 2):
        pairs.append((positions[i], positions[i+1]))
    return [f"{i+1}{j+1}" for i, j in enumerate(pairs)]

T = int(input())
for case in range(T):
    N = int(input())
    positions = []
    for _ in range(2*N):
        x, y = map(int, input().split())
        positions.append((x, y))
    
    result = find_magnificent_arrangement(N, positions)
    print(f"Case #{case+1}: {' '.join(result)}")