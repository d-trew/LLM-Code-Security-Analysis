def max_rhymes(words):
    def is_rhyme(word1, word2):
        return word1[::-1][:len(word1) - len(word1.rstrip('A'))] == \
               word2[::-1][:len(word2) - len(word2.rstrip('A'))]
    words = sorted(words, key=lambda x: (x[:-1].count('A'), x))
    dp = [0] * len(words)
    for i in range(len(dp)):
        dp[i] = 1 + max((dp[j] for j in range(i) if is_rhyme(words[i], words[j])), default=0)
    return max(dp)

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    words = [input() for _ in range(N)]
    print("Case #{}: {}".format(case, max_rhymes(words)))