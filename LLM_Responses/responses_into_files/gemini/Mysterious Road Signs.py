def solve():
    S = int(input())
    signs = []
    for _ in range(S):
        D, A, B = map(int, input().split())
        signs.append((D, A, B))

    max_signs = 0
    count = 0

    for i in range(1 << S):
        subset = []
        for j in range(S):
            if (i >> j) & 1:
                subset.append(signs[j])

        if not subset:
            continue

        valid = False
        for M in range(1, 1001):  # Adjust range as needed
            for N in range(-1000, 1001): # Adjust range as needed
                consistent = True
                for k in range(len(subset)):
                    if subset[k][1] != M + subset[k][0] or subset[k][2] != N + (subset[-1][0] - subset[k][0]):
                        consistent = False
                        break
                if consistent:
                    valid = True
                    break
            if valid:
                break

        if valid:
            num_signs = len(subset)
            if num_signs > max_signs:
                max_signs = num_signs
                count = 1
            elif num_signs == max_signs:
                count += 1

    return max_signs, count

T = int(input())
for i in range(1, T + 1):
    result_signs, result_count = solve()
    print(f"Case #{i}: {result_signs} {result_count}")