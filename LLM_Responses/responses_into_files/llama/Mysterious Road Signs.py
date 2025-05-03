def count_signs(S):
    max_length = 0
    sets = {}
    for i in range(S):
        d, A, B = map(int, input().split())
        if i == 0:
            max_length += 1
        elif A > max_length - 1 or B < i + 1 - max_length:
            max_length = min(A, B)
        sets.setdefault(max_length, []).append((d, A, B))
    return str(S) + ' ' + str(len(sets.get(max_length, [])))