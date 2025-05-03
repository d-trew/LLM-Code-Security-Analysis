import collections
import itertools

def max_fakes(topics):
    word_count = collections.Counter(itertools.chain(*topics))
    used_words = set(word for _, word in topics)

    faker_combs = []
    for first, second in itertools.product(used_words, repeat=2):
        comb = ''.join((first, second))
        if comb not in used_words and (comb[0] != second or comb[1] != first):
            faker_combs.append(comb)

    return len(faker_combs)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    topics = [list(map(str.upper, input().split())) for _ in range(N)]
    print(f"Case #{t}: {max_fakes(topics)}")