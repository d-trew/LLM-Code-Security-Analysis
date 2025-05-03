import sys
from itertools import combinations
input = sys.stdin.readline

def solve(N, L):
    tiles = set()
    words = []
    for _ in range(N):
        word = input().strip()
        if word not in words:
            words.append(word)
            tiles |= set(word)
    tiles -= {'A'}
    if len(tiles) < L:
        return '-'
    new_words = ["".join(c) for c in combinations(tiles, L)]
    return "\n".join(filter(lambda w: w not in words, new_words))

T = int(input())
for _ in range(T):
    N, L = map(int, input().split())
    print(f"Case #{_+1}: {solve(N, L)}")


This Python code reads the number of test cases from the standard input, then iterates through each test case. For each test case, it first initializes an empty set `tiles` and a list `words`. It reads the words given by Vincent one by one and adds them to `words` while also adding their unique letters to `tiles`. If there are not enough unique letters in `tiles` to create a word of length `L`, it returns "-". Otherwise, it generates all possible combinations of `L` letters from `tiles` using the itertools.combinations function and filters out any words that are already in Vincent's list of words. Finally, it returns the resulting list of new words joined by newlines. The output is printed for each test case with a prefix indicating the case number.