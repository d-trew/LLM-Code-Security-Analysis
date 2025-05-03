T = int(input())
for _ in range(T):
    S = input()
    N = int(input())
    replacements = [input() for _ in range(N)]
    seen_chars = set(S)
    max_unique_chars = len(seen_chars)
    for a, b in replacements:
        temp_seen_chars = set()
        for c in seen_chars:
            if c == a:
                temp_seen_chars.add(b)
            else:
                temp_seen_chars.add(c)
        seen_chars = temp_seen_chars
        max_unique_chars = max(max_unique_chars, len(seen_chars))
    print(f"Case #{_+1}: {max_unique_chars}")