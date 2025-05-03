import itertools

def find_largest_rhyming_subset(words):
    max_size = 0
    for p in range(1, len(words) + 1):
        for accentuations in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=len(words)):
            if all(words[i][word.find(accents[i]):] == words[j][word.find(accents[j]):] for i in range(p) for j in range(i+1, p)):
                max_size = max(max_size, p)
    return max_size

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    words = [input().upper() for _ in range(N)]
    print(f"Case #{t}: {find_largest_rhyming_subset(words)}")