def count_visible_pillars(N, R):
    if N == 1:
        return 0
    radius_m = R / 1e6
    grid_size = 2 * radius_m
    visible_count = 0

    for i in range(1, N):
        for j in range(1, N):
            distance_squared = (i - 0.5) ** 2 + (j - 0.5) ** 2
            if distance_squared > grid_size ** 2:
                visible_count += 1

    return visible_count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    index = 1
    results = []

    for _ in range(T):
        N = int(data[index])
        R = float(data[index + 1])
        index += 2

        result = count_visible_pillars(N, R)
        results.append(f"Case #{_+1}: {result}")

    print("\n".join(results))

if __name__ == "__main__":
    main()