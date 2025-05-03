def solve(K, C, S):
    if K * (C - 1) < S:
        return "IMPOSSIBLE"
    else:
        return [i for i in range(2, S + 1)] + [1]

T = int(input())
for tc in range(1, T + 1):
    K, C, S = map(int, input().split())
    result = solve(K, C, S)
    print("Case #{}: {}".format(tc, " ".join(map(str, result)) if type(result) == list else result))