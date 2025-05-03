def find_median_order(T, N, Q):
    for _ in range(T):
        elements = list(range(1, N + 1))
        while len(elements) > 1:
            if len(elements) == 3:
                i, j, k = elements
                l = int(input(f"{i} {j} {k}\n"))
                if l not in [i, j, k]:
                    return -1
                elements.remove(l)
            else:
                mid = len(elements) // 2
                i, j, k = elements[mid - 1], elements[mid], elements[mid + 1]
                l = int(input(f"{i} {j} {k}\n"))
                if l not in [i, j, k]:
                    return -1
                elements.remove(l)
        print(elements[0])

# Read input
T, N, Q = map(int, input().split())
find_median_order(T, N, Q)