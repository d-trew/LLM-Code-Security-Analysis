def find_new_word(vincent_words):
    # Create a set of all letters in the words Vincent has
    vincent_letters = set(''.join(vincent_words))
    
    # Iterate over all possible 2-letter combinations
    for i in range(65, 91):
        for j in range(i+1, 91):
            new_word = chr(i) + chr(j)
            
            # If the new word is not a subset of any Vincent's words and does not contain any letters that Vincent has
            if all(not set(new_word).issubset(set(word)) for word in vincent_words) and not set([chr(i), chr(j)]).issubset(vincent_letters):
                return new_word
    
    # If no valid new words are found, return '-'
    return '-'

T = int(input())
for case in range(1, T + 1):
    N, L = map(int, input().split())
    vincent_words = [input() for _ in range(N)]
    
    print('Case #{}: {}'.format(case, find_new_word(vincent_words)))