def find_atomic_weights(N, molecules):
    for c in range(1, 101):
        for j in range(1, 101):
            if all(c * ci + j * ji == (c * ci2 + j * ji2) // 2 for ci, ji, ci2, ji2 in zip(molecules[:-1], molecules[1:])):
                return c, j
    return "IMPOSSIBLE"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        molecules = [(int(data[index + 2 * i]), int(data[index + 2 * i + 1])) for i in range(N)]
        index += 2 * N
        result = find_atomic_weights(N, molecules)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i + 1}: {result}")

if __name__ == "__main__":
    main()