def assign_blocks(R, C, S, stations):
    grid = [[0] * C for _ in range(R)]
    assigned = [0] * S

    def is_patrollable(r, c, ri, ci, di):
        return abs(r - ri) <= di and abs(c - ci) <= di

    for i in range(S):
        ri, ci, di = stations[i]
        ri -= 1
        ci -= 1
        for r in range(R):
            for c in range(C):
                if is_patrollable(r, c, ri, ci, di):
                    grid[r][c] = i + 1

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                continue
            assigned[grid[r][c] - 1] += 1

    min_blocks = min(assigned)
    max_blocks = max(assigned)
    return max_blocks - min_blocks

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    T = int(data[index])
    index += 1
    results = []

    for _ in range(T):
        R = int(data[index])
        C = int(data[index + 1])
        S = int(data[index + 2])
        index += 3

        stations = []
        for i in range(S):
            ri = int(data[index])
            ci = int(data[index + 1])
            di = int(data[index + 2])
            index += 3
            stations.append((ri, ci, di))

        result = assign_blocks(R, C, S, stations)
        results.append(f"Case #{_ + 1}: {result}")

    for result in results:
        print(result)

if __name__ == "__main__":
    main()