def find_new_word(N, L, words):
    from collections import Counter
    
    # Count the frequency of each character and number combination
    tile_counts = Counter()
    for word in words:
        for char, num in zip(word, range(1, L+1)):
            tile_counts[(char, num)] += 1
    
    # Try to form a new word
    for i in range(ord('A'), ord('Z') + 1):
        for j in range(1, L + 1):
            if (chr(i), j) not in tile_counts:
                continue
            new_word = chr(i)
            remaining_tiles = tile_counts.copy()
            remaining_tiles[(chr(i), j)] -= 1
            found = True
            for k in range(2, L + 1):
                if (new_word[k-1], k) not in remaining_tiles or remaining_tiles[(new_word[k-1], k)] == 0:
                    found = False
                    break
                else:
                    remaining_tiles[(new_word[k-1], k)] -= 1
            if found:
                return chr(i)
    return '-'

# Read input
T = int(input())
results = []
for t in range(1, T + 1):
    N, L = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    result = find_new_word(N, L, words)
    results.append(f"Case #{t}: {result}")

# Output results
for result in results:
    print(result)