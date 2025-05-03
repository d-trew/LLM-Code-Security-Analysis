from itertools import product

T = int(input())
for t in range(1, T + 1):
    C, J = input().split()
    min_diff = float('inf')
    result_C, result_J = None, None
    for c, j in product(map(int, '0123456789'), repeat=len(C)):
        if str(c) == C.replace('?','0') and str(j) == J.replace('?','0'):
            diff = abs(int(str(c)) - int(str(j)))
            if diff < min_diff:
                min_diff = diff
                result_C, result_J = str(c), str(j)
    print(f"Case #{t}: {result_C} {result_J}")