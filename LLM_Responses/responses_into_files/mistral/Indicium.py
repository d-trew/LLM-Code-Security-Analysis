from itertools import permutations

def is_valid_natural_latin_square(n, latin_square):
    for i in range(n):
        row = set()
        col = set()
        for j in range(n):
            if latin_square[i][j] in row:
                return False
            row.add(latin_square[i][j])
            if latin_square[j][i] in col:
                return False
            col.add(latin_square[j][i])
    return True

def calculate_trace(n, latin_square):
    trace = 0
    for i in range(n):
        trace += latin_square[i][i]
    return trace

def find_natural_latin_square(n, k):
    if n > k:
        return "IMPOSSIBLE"
    for latin_square in permutations(range(1, n+1), n*n).reshape((n,n)):
        if is_valid_natural_latin_square(n, latin_square) and calculate_trace(n, latin_square) == k:
            return latin_square
    return "IMPOSSIBLE"

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    result = find_natural_latin_square(N, K)
    if result == "IMPOSSIBLE":
        print("Case #{}: {}".format(t+1, result))
    else:
        print("Case #{}: POSSIBLE".format(t+1))
        for row in result:
            print(' '.join(map(str, row)))