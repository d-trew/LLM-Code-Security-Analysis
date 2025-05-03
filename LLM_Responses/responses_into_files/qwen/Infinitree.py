def find_distance(N, A, B, L, R):
    def get_parent(index):
        return (index - 1) // 2 + 1

    def get_children(parent):
        left = parent * 2 - 1
        right = parent * 2
        if left > N:
            left = None
        if right > N:
            right = None
        return left, right

    while A != B:
        if A < B:
            A = get_parent(A)
        else:
            B = get_parent(B)

    return abs(A - B) + 1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    index = 1
    results = []

    for _ in range(T):
        N = int(data[index])
        A = int(data[index + 1]) - 1
        B = int(data[index + 2]) - 1
        L = list(map(int, data[index + 3:index + 3 + N]))
        R = list(map(int, data[index + 3 + N:index + 6 + N]))

        index += 6 + N

        result = find_distance(N, A, B, L, R)
        results.append(f"Case #{_ + 1}: {result}")

    for result in results:
        print(result)

if __name__ == "__main__":
    main()