def can_place_printer(fences, position):
    for fence in fences:
        if (fence[0][0] <= position[0] <= fence[1][0] or
            fence[0][0] >= position[0] >= fence[1][0]) and \
           (fence[0][1] <= position[1] <= fence[1][1] or
            fence[0][1] >= position[1] >= fence[1][1]):
            return False
    return True

def find_order(fences, K):
    order = list(range(1, len(fences) + 1))
    for i in range(K):
        for j in range(i + 1, len(order)):
            if not can_place_printer(fences[:i] + fences[j:j+1] + fences[i+1:j], (fences[i][0][0], fences[i][0][1])):
                order[i], order[j] = order[j], order[i]
    return ' '.join(map(str, order))

T = int(input())
for t in range(1, T + 1):
    F, K = map(int, input().split())
    fences = []
    for _ in range(F):
        A, B, C, D = map(int, input().split())
        if A == C and B < D:
            fences.append(((A, B), (C, D)))
        else:
            fences.append(((C, D), (A, B)))
    result = find_order(fences, K)
    print(f"Case #{t}: {result}")