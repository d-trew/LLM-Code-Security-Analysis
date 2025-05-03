import sys

def largest_subset(words):
    accented_words = []
    for word in words:
        if len(word) > 1 and word[0] == 'J':
            accented_words.append(word)
    if not accented_words:
        return 0
    pairs = []
    for i, word in enumerate(accented_words):
        for j, other_word in enumerate(accented_words):
            if i != j and word[-1] == other_word[-1]:
                pairs.append((word, other_word))
    return len(pairs) + 1

if __name__ == '__main__':
    test_cases = int(input())
    for case in range(1, test_cases+1):
        words = []
        n = int(input())
        for _ in range(n):
            word = input()
            if len(word) > 1 and word[0] == 'J':
                words.append(word)
        print('Case #{}'.format(case), largest_subset(words))