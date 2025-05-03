T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().split())
    words = [input() for _ in range(N)]
    seen = set(word[:L] for word in words)
    possible_words = []
    for word in words:
        for i in range(len(words) - len(word) + 1):
            if ''.join([c[i] for c in word]) not in seen and len(word) == L:
                possible_words.append(''.join([c[i] for c in word]))
    if possible_words:
        print(f"Case #{t}: {'- ' if not possible_words[0].isalpha() else possible_words[0]}")
    else:
        print(f"Case #{t}: -")