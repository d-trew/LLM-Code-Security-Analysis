def solve(patterns):
    common_chars = [None] * 26
    for pattern in patterns:
        for i, c in enumerate([ord(c) - ord('A') for c in pattern if c != '*']):
            if not (0 <= c < 26): continue
            if common_chars[c] is None:
                common_chars[c] = [pattern[i]]
            elif len(common_chars[c]) == i or common_chars[c][i] != pattern[i]:
                return "*"
    name = ''.join([chr(ord('A') + c) for c in range(26) if common_chars[c] is not None])
    return name

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    patterns = [input().strip() for _ in range(N)]
    print("Case #{}: {}".format(t, solve(patterns)))