def count_geese_choices(N, C, A, B, P):
    from itertools import combinations

    def is_valid_set(s):
        color_count = [0] * (C + 1)
        for i in s:
            color_count[P[i]] += 1
        return all(A[c] <= color_count[c] <= B[c] for c in range(1, C + 1))

    total_choices = 0
    for length in range(2, N):
        for start in range(N - length + 1):
            subset = set(range(start, start + length))
            if is_valid_set(subset):
                total_choices += 1

    return total_choices

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    T = int(data[index])
    index += 1
    results = []

    for _ in range(T):
        N = int(data[index])
        C = int(data[index + 1])
        A = [0] * (C + 1)
        B = [0] * (C + 1)
        P = []
        index += 2

        for i in range(C):
            A[i + 1] = int(data[index])
            B[i + 1] = int(data[index + 1])
            index += 2

        for _ in range(N):
            P.append(int(data[index]))
            index += 1

        result = count_geese_choices(N, C, A, B, P)
        results.append(f"Case #{_+1}: {result}")

    print("\n".join(results))

if __name__ == "__main__":
    solve()